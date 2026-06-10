"""Flask webapp — Kiểm Tra Online — Gia Đình SU KHÔI MÈO."""
import ipaddress
import os
import random
import time
import json
from datetime import datetime, timezone, timedelta
from urllib.parse import urlparse
from flask import Flask, render_template, request, redirect, url_for, session, flash

import markdown as md_lib
import markitdown_client as md_client
from markitdown_client import MarkItDownError

import questions

app = Flask(__name__)
app.secret_key = "kiemtra-sukhoikem-2026"

# Giờ Hà Nội (UTC+7, không có DST) — production DO chạy UTC nên phải ép múi giờ
_HANOI_TZ = timezone(timedelta(hours=7))
def _now_hanoi() -> str:
    """Trả về ISO timestamp theo giờ Hà Nội, vd '2026-06-09T19:22:18+07:00'."""
    return datetime.now(_HANOI_TZ).isoformat(timespec="seconds")

# Prod (DigitalOcean): Postgres qua DATABASE_URL -> dữ liệu sống qua mỗi lần
# deploy. Local: SQLite file. Đĩa của App Platform là ephemeral nên SQLite
# trên prod sẽ mất sạch lịch sử mỗi lần deploy/restart.
DATABASE_URL = os.environ.get("DATABASE_URL", "").strip()
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = "postgresql://" + DATABASE_URL[len("postgres://"):]
USE_PG = DATABASE_URL.startswith("postgresql://")

if USE_PG:
    import psycopg
    from psycopg.rows import dict_row
else:
    import sqlite3
    _DATA_DIR = os.environ.get("DATA_DIR", os.path.dirname(__file__))
    DB_PATH = os.path.join(_DATA_DIR, "kiemtra.db")


def get_db():
    if USE_PG:
        return psycopg.connect(DATABASE_URL, row_factory=dict_row)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def _ph(sql):
    return sql.replace("?", "%s") if USE_PG else sql


def init_db():
    pk = "SERIAL PRIMARY KEY" if USE_PG else "INTEGER PRIMARY KEY AUTOINCREMENT"
    conn = get_db()
    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS attempts (
            id {pk},
            student TEXT NOT NULL,
            student_key TEXT NOT NULL DEFAULT 'bao_meo',
            mode TEXT NOT NULL,
            duration INTEGER NOT NULL,
            score INTEGER NOT NULL,
            total INTEGER NOT NULL,
            time_used INTEGER NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS exam_progress (
            id {pk},
            student_key TEXT NOT NULL,
            folder TEXT NOT NULL,
            exam_no INTEGER NOT NULL,
            score INTEGER,
            completed_at TEXT NOT NULL
        )
    """)
    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS documents (
            id {pk},
            title TEXT NOT NULL,
            source TEXT,
            markdown TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    # Migration: bổ sung cột exam_no + results_json cho bảng attempts cũ
    for coldef in ("exam_no INTEGER DEFAULT 1", "results_json TEXT"):
        try:
            conn.execute(f"ALTER TABLE attempts ADD COLUMN {coldef}")
            conn.commit()
        except Exception:
            conn.rollback()  # cột đã tồn tại → bỏ qua
    conn.commit()
    conn.close()


init_db()

# ── MarkItDown helpers ─────────────────────────────────────────────────────────

_UPLOAD_MAX_BYTES = 25 * 1024 * 1024   # 25 MB
_ALLOWED_EXTS = {".pdf", ".docx", ".pptx", ".xlsx", ".html", ".htm",
                 ".txt", ".md", ".csv", ".xml"}

_PRIVATE_NETS = [
    ipaddress.ip_network("10.0.0.0/8"),
    ipaddress.ip_network("172.16.0.0/12"),
    ipaddress.ip_network("192.168.0.0/16"),
    ipaddress.ip_network("127.0.0.0/8"),
    ipaddress.ip_network("169.254.0.0/16"),
    ipaddress.ip_network("::1/128"),
    ipaddress.ip_network("fc00::/7"),
]


def _validate_crawl_url(url: str) -> str:
    """Chỉ cho phép HTTPS và không cho địa chỉ nội bộ (chống SSRF)."""
    parsed = urlparse(url.strip())
    if parsed.scheme != "https":
        raise ValueError("Chỉ chấp nhận URL dạng https://")
    host = (parsed.hostname or "").lower()
    if not host or host in ("localhost",):
        raise ValueError("URL không hợp lệ.")
    try:
        addr = ipaddress.ip_address(host)
        for net in _PRIVATE_NETS:
            if addr in net:
                raise ValueError("Không cho phép địa chỉ IP nội bộ.")
    except ValueError as exc:
        if "does not appear to be" not in str(exc):
            raise
    return url.strip()


def _save_document(conn, title: str, source: str, markdown: str) -> int:
    now = _now_hanoi()
    if USE_PG:
        cur = conn.execute(
            "INSERT INTO documents (title, source, markdown, created_at)"
            " VALUES (%s,%s,%s,%s) RETURNING id",
            (title, source, markdown, now),
        )
        row = cur.fetchone()
        conn.commit()
        return row["id"]
    cur = conn.execute(
        "INSERT INTO documents (title, source, markdown, created_at) VALUES (?,?,?,?)",
        (title, source, markdown, now),
    )
    conn.commit()
    return cur.lastrowid

EXTS = (".png", ".jpg", ".jpeg", ".webp", ".jfif")
ICON_BASE = os.path.join(os.path.dirname(__file__), "static", "icons")


def load_icons(subdir):
    d = os.path.join(ICON_BASE, subdir)
    if not os.path.isdir(d):
        return []
    return sorted([f for f in os.listdir(d) if f.lower().endswith(EXTS)])


def load_icons_multi(subdirs):
    """Load icons from multiple subdirs, return list of 'subdir/filename' strings."""
    result = []
    for sub in subdirs:
        d = os.path.join(ICON_BASE, sub)
        if os.path.isdir(d):
            for f in sorted(os.listdir(d)):
                if f.lower().endswith(EXTS):
                    result.append(f"{sub}/{f}")
    return result



STUDENT_THEMES = {
    "bao_meo": {
        "name": "Bảo Mèo", "icon": "🐱",
        "primary": "#ff7eb6", "bg": "#fff8fb",
        "css": "theme-pink", "icon_dir": "bao_meo",
        "icon_dirs": ["bao_meo"],
        "grades": "Lớp 1D",
        "has_audio": False,
    },
    "minh_khanh": {
        "name": "Minh Khanh", "icon": "🌸",
        "primary": "#c084fc", "bg": "#fdf4ff",
        "css": "theme-purple", "icon_dir": "minh_khanh",
        "icon_dirs": ["minh_khanh", "minh_khanh_harry", "minh_khanh_cinamoroll"],
        "grades": "Lớp 6A3",
        "has_audio": True,
    },
    "nhat_khoi": {
        "name": "Nhật Khôi", "icon": "⚡",
        "primary": "#38bdf8", "bg": "#f0f9ff",
        "css": "theme-blue", "icon_dir": "nhat_khoi",
        "icon_dirs": ["nhat_khoi", "nhat_khoi_harry"],
        "grades": "Lớp 8A1",
        "has_audio": False,
    },
    "tip_nicolas": {
        "name": "Tip Nicolas", "icon": "🤖",
        "primary": "#dc2626", "bg": "#f4f4f5",
        "css": "theme-gundam", "icon_dir": "tip_nicolas",
        "icon_dirs": ["tip_nicolas"],
        "grades": "Lớp 6",
        "has_audio": False,
    },
}

DUR_TO_NQ = {45: 15, 60: 20, 90: 30}

HSG_ANH_DRIVE_IDS = {
    1:  "1b8TlXE0jlLCOP0vqT9OcGj1jaVGs8A5q",
    2:  "1QXEDqCsSWAhdzyyar24oUM4B76XvlkCH",
    3:  "1OnyYuc5SgZrsndDJvJqisRbzE7eM-zTl",
    4:  "1vZITTX1UWJHaVVc7wc5eQhWTf9enq9Qa",
    5:  "1lgV0FQkx_LlGBXIhtJ8AIVAc0vXJa18w",
    6:  "19fqtYLKQuSkS89Mf_IzHByNozFz9LDhd",
    7:  "1C1iS-S5JIVBD_vlG_wrXMUzfT4Mu6a6g",
    8:  "1xOZWcqpFwurVAqfm9zTif9QpQOcaZn_1",
    9:  "1Nthxs3aVNLH0LqswTrSYhTtiFY5i439a",
    10: "118GxVGd6ig-81wfFpBlmtPuR8RKOuURP",
    11: "1oEi-WyQiRTqZLQZ8hXf2R3estky31NGK",
    12: "1Gq_sdKbDJiTZW04BIEVIrBXaa3XZMavM",
    13: "1XcPHpzRYO1FqblIZ_r732bDdaXOUrQQe",
    14: "1YxXsGajF4b6tM-RT3TU0Upwq8SRuf-UF",
    15: "1XJlC-IfTaCyy-A45-7CXiEbsw9EiNHmo",
    16: "1mgwClxuQsFA9YmupbJcOi8vANSCnr667",
    17: "1lCq9ZCY0BItYGUyoLlB47qlkutSvpR-3",
    18: "1u7FG13oaJLhJhTp9m73YKlvfwKQnVURJ",
    19: "1seEaRDL_RL1MqhM2iacDw9go7JrTnxG4",
    20: "1Ytwa8PwJFwXnPjBrAhRPMCewgd-WZle1",
    21: "1w7fr45HQxUqqnLKwCwgsndms9SJ18G5P",
    22: "1ZAd_VM4XxYdwpoabCT-M5KuFASUnKmDO",
    23: ["19_L20qj_Dgn8qbYIVuUItr8kByCTcam9", "1DhTMOCHNOtckiQqs0NRz3ACZX6B8rqj3", "1msbVLMCAKvHnGqPUvs70uaZlY9RehLIf"],
    24: "1DA2VxjTPRCGzI2IVfnbXUvxS0SQ8EOl4",
    25: "1GEB1BlAHOjjKCR07vRfTefl9R-pBT3-C",
    26: "1-PhH-nfSw1WtNimqN4V8t5_nUnTbYH5d",
    27: "1aQM-IZZdbf-x92T2wGwj_Zr45L8sdy8-",
    28: "1FXoZRRlBHcwam3IcpL0XMAh7zvFTuD2V",
    29: "1Kf4qGLVnd04k7aQ5fTILL5oX0GX8CL9k",
    30: "1fl7k-s9802g29Cr051hZVjwVfcEX2-11",
    31: ["1-VVGM62Hw4ivPC8ujKNrAsmjvOFBF0xn", "1kn1LhSGutqk0VpINmdpo57KF0szazJeJ"],
    32: "1WOzeflcxxyymE2sN1EnteQ_qTC4XjfVS",
    33: "16HZueaSMiLckRImvbDIcMD5TXFBXtZm2",
    34: "1UmW2LNEmsqDXwBmpaXZg7VQ5UN-xYS9z",
    35: "1dUAkm_LWCNlNnGBL7u1LNOt5JYdEzGPX",
    36: "1WhIt0VeNaPfI__j3mqvQAV_O43VjbjU6",
}

FOLDER_EXAM_COUNTS = {
    # Lớp 2 (agent-crawled — tăng tự động khi có thêm câu hỏi)
    "toan_2_hk1":       5,
    "toan_2_hk2":       5,
    "de_hsg_toan_2":    5,
    "toan_violympic_2": 5,
    "tieng_anh_2_hk1":  5,
    "tieng_anh_2_hk2":  5,
    # Lớp 1
    "de_hk2_toan_1":      15,   # pool random từ 2 đề PDF + 28 câu NC + 200 câu mới → 15 lần bốc khác nhau
    "toan_violympic_1":   29,   # 19 vòng gốc + 10 vòng mới, pool 366 câu hard random 30/vòng
    "de_hsg_toan_1":      30,   # 20 đề × 30 câu hard pool (DE_11–20 + DE_ON) + 250 câu mới
    # Lớp 6
    "de_toan_6_hk2":       9,   # 9 PDF đề đơn
    "de_olympic_toan_6":  29,   # 10 đề đơn + VIOLYMPIC TOÁN 6 có 19 vòng
    "de_hsg_toan_6":      11,   # 11 PDF đề HSG cấp trường/xã
    "de_hsg_anh_6":        36,   # 36 đề HSG Anh 6 (mỗi đề có file MP3)
    "de_tieng_anh_6_hk2": 10,   # 5 đề Lớp 6 + 5 đề Lớp 8
    # Lớp 7
    "toan_7_hk1":         14,   # 14 PDF đề đơn
    "toan_7_hk2":          5,   # pool chung với HK1, random 5 vòng
    "tieng_anh_7_hk1":    29,   # 29 PDF đề đơn
    "tieng_anh_7_hk2":     5,   # 50 câu mới
    # Lớp 8
    "toan_8_hk1":          5,   # 55 câu mới
    "toan_8_hk2":         16,   # 6 PDF + 10 docx đề đơn
    "tieng_anh_8_hk1":     5,   # 55 câu mới
    "tieng_anh_8_hk2":     5,   # 55 câu mới
}


def get_theme(student_key):
    return STUDENT_THEMES.get(student_key, STUDENT_THEMES["bao_meo"])


@app.route("/")
def index():
    content_tree_json = json.dumps([
        {"key": lk, "display": ld,
         "folders": [{"key": fk, "display": fd} for fk, fd in folders]}
        for lk, ld, folders in questions.CONTENT_TREE
    ])
    conn = get_db()
    rows = conn.execute(
        "SELECT student_key, folder, exam_no FROM exam_progress WHERE score >= 7"
    ).fetchall()
    conn.close()
    completed: dict = {}
    for row in rows:
        sk, f, n = row["student_key"], row["folder"], row["exam_no"]
        completed.setdefault(sk, {}).setdefault(f, set()).add(n)
    completed_json = json.dumps({
        sk: {f: sorted(nums) for f, nums in folders.items()}
        for sk, folders in completed.items()
    })
    # Capacity per folder: max questions achievable
    capacities = {}
    for lk, _, folders in questions.CONTENT_TREE:
        for fk, _ in folders:
            capacities[fk] = questions.folder_capacity(lk, fk)
    return render_template(
        "index.html",
        themes=STUDENT_THEMES,
        content_tree_json=content_tree_json,
        folder_exam_counts_json=json.dumps(FOLDER_EXAM_COUNTS),
        completed_json=completed_json,
        folder_capacities_json=json.dumps(capacities),
        hsg_exam_nq_json=json.dumps(questions.HSG_EXAM_NQ),
        hsg_exam_dur_json=json.dumps(questions.HSG_EXAM_DURATIONS),
        hsg_anh_exam_nq_json=json.dumps(questions.HSG_ANH_EXAM_NQ),
        hsg_anh_exam_dur_json=json.dumps(questions.HSG_ANH_EXAM_DURATIONS),
        hsg_toan_1_exam_nq_json=json.dumps(questions.HSG_TOAN_1_NQ),
        hsg_toan_1_exam_dur_json=json.dumps(questions.HSG_TOAN_1_DURATIONS),
        violympic_toan_1_nq_json=json.dumps(questions.VIOLYMPIC_TOAN_1_NQ),
        violympic_toan_1_dur_json=json.dumps(questions.VIOLYMPIC_TOAN_1_DURATIONS),
    )


@app.route("/start", methods=["POST"])
def start():
    student_key = request.form.get("student_key", "bao_meo")
    theme = get_theme(student_key)
    student = theme["name"]
    lop = request.form.get("lop", "lop_1")
    folder = request.form.get("folder", "de_hk2_toan_1")
    exam_no = int(request.form.get("exam_no", 1))

    if folder == "de_hsg_toan_6":
        duration = questions.HSG_EXAM_DURATIONS.get(exam_no, 120)
        n_q = questions.HSG_EXAM_NQ.get(exam_no, 10)
    elif folder == "de_hsg_anh_6":
        duration = questions.HSG_ANH_EXAM_DURATIONS.get(exam_no, 120)
        n_q = questions.HSG_ANH_EXAM_NQ.get(exam_no, 0)
    elif folder == "de_hsg_toan_1":
        duration = questions.HSG_TOAN_1_DURATIONS.get(exam_no, 60)
        n_q = questions.HSG_TOAN_1_NQ.get(exam_no, 10)
    elif folder == "toan_violympic_1":
        duration = questions.VIOLYMPIC_TOAN_1_DURATIONS.get(exam_no, 45)
        n_q      = questions.VIOLYMPIC_TOAN_1_NQ.get(exam_no, 30)
    else:
        duration = int(request.form.get("duration", 45))
        n_q = int(request.form.get("n_questions", DUR_TO_NQ.get(duration, 15)))

    seed = int(time.time() * 1000) % 1_000_000

    session["student"] = student
    session["student_key"] = student_key
    session["lop"] = lop
    session["folder"] = folder
    session["duration"] = duration
    session["exam_no"] = exam_no
    session["seed"] = seed
    session["n_q"] = n_q
    session["start_time"] = time.time()
    return redirect(url_for("exam"))


@app.route("/exam")
def exam():
    seed = session.get("seed")
    if seed is None:
        return redirect(url_for("index"))
    lop = session.get("lop", "lop_1")
    folder = session.get("folder", "de_hk2_toan_1")
    n_q = session.get("n_q", 15)
    exam_no = session.get("exam_no", 1)
    qs = questions.gen_exam(lop, folder, n=n_q, seed=seed, exam_no=exam_no)
    student_key = session.get("student_key", "bao_meo")
    theme = get_theme(student_key)
    icons = load_icons_multi(theme["icon_dirs"])
    random.shuffle(icons)
    if folder == "de_hsg_anh_6":
        raw = HSG_ANH_DRIVE_IDS.get(exam_no, "")
        ids = raw if isinstance(raw, list) else ([raw] if raw else [])
        audio_files = [f"https://drive.google.com/file/d/{d}/view" for d in ids]
        audio_label = "A. LISTENING — Nhấn nút bên dưới để mở file nghe (mở tab mới)."
        subject = "Tiếng Anh"
    else:
        audio_files = []
        audio_label = ""
        subject = "Tiếng Anh" if "tieng_anh" in folder or "anh" in folder else "Toán"
    return render_template(
        "exam.html",
        questions=qs,
        duration=session.get("duration", 45),
        student=session.get("student", "Bé"),
        student_key=student_key,
        folder_name=questions.folder_display(lop, folder),
        theme=theme,
        icons=icons,
        audio_files=audio_files,
        audio_label=audio_label,
        subject=subject,
        body_class=theme["css"],
    )


@app.route("/submit", methods=["POST"])
def submit():
    seed = session.get("seed")
    if seed is None:
        return redirect(url_for("index"))
    lop = session.get("lop", "lop_1")
    folder = session.get("folder", "de_hk2_toan_1")
    n_q = session.get("n_q", 15)
    exam_no = session.get("exam_no", 1)
    qs = questions.gen_exam(lop, folder, n=n_q, seed=seed, exam_no=exam_no)
    if not qs:
        return redirect(url_for("index"))

    student = session.get("student", "Bé")
    student_key = session.get("student_key", "bao_meo")
    theme = get_theme(student_key)
    duration = session.get("duration", 45)
    start_time = session.get("start_time", time.time())
    time_used = int(time.time() - start_time)

    score = 0
    results = []
    norm = lambda s: s.lower().replace(" ", "")
    for i, q in enumerate(qs):
        multi_answers = q.get("answers")
        if isinstance(multi_answers, list):
            # Multi-answer: tính điểm theo số ô đúng / tổng ô
            labels = q.get("answer_labels", [])
            parts_correct = 0
            user_parts = []
            for j, expected in enumerate(multi_answers):
                user_part = request.form.get(f"q_{i}_{j}", "").strip()
                part_ok = norm(user_part) == norm(str(expected))
                if part_ok:
                    parts_correct += 1
                label = labels[j] if j < len(labels) else f"Phần {j+1}"
                user_parts.append(f"{label}: {user_part or '(trống)'}")
            score += parts_correct / len(multi_answers)
            ok = (parts_correct == len(multi_answers))
            user_ans = "; ".join(user_parts)
            correct = "; ".join(
                f"{(labels[j] if j < len(labels) else f'Phần {j+1}')}: {v}"
                for j, v in enumerate(multi_answers)
            )
        else:
            user_ans = request.form.get(f"q_{i}", "").strip()
            correct = str(q.get("answer", "")).strip()
            ok = norm(user_ans) == norm(correct) or any(
                norm(user_ans) == norm(alt) for alt in q.get("alt_answers", [])
            )
            if ok:
                score += 1
        results.append({"q": q["q"], "your": user_ans or "(không trả lời)",
                         "correct": correct, "ok": ok, "topic": q.get("topic", ""),
                         "explanation": q.get("explanation", ""),
                         "image": q.get("image", "")})

    total = len(qs)
    score_10 = round(score * 10 / total) if total else 0
    exam_no = session.get("exam_no", 1)

    conn = get_db()
    conn.execute(
        _ph("INSERT INTO attempts (student, student_key, mode, duration, score, total, time_used, created_at, exam_no, results_json)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"),
        (student, student_key, folder, duration, score_10, total, time_used,
         _now_hanoi(), exam_no,
         json.dumps(results, ensure_ascii=False)),
    )
    conn.execute(
        _ph("INSERT INTO exam_progress (student_key, folder, exam_no, score, completed_at)"
            " VALUES (?, ?, ?, ?, ?)"),
        (student_key, folder, exam_no, score_10,
         _now_hanoi()),
    )
    conn.commit()
    conn.close()

    all_icons = load_icons_multi(theme["icon_dirs"])
    session.pop("seed", None)
    return render_template(
        "result.html",
        student=student, student_key=student_key,
        folder_name=questions.folder_display(lop, folder), theme=theme,
        score=score_10, raw_score=score, total=total,
        time_used=time_used, results=results,
        icons_json=json.dumps(all_icons),
        body_class=theme["css"],
    )


@app.route("/history")
def history():
    conn = get_db()
    rows = conn.execute(
        "SELECT * FROM attempts ORDER BY created_at DESC LIMIT 200"
    ).fetchall()
    conn.close()
    by_day = {}
    for r in rows:
        day = r["created_at"][:10]
        by_day.setdefault(day, []).append(dict(r))
    return render_template("history.html", attempts=rows, by_day=by_day)


@app.route("/history/<int:attempt_id>")
def history_detail(attempt_id):
    conn = get_db()
    row = conn.execute(
        _ph("SELECT * FROM attempts WHERE id = ?"), (attempt_id,)
    ).fetchone()
    conn.close()
    if not row:
        return redirect(url_for("history"))
    a = dict(row)
    results = []
    raw_json = a.get("results_json")
    if raw_json:
        try:
            results = json.loads(raw_json)
        except (ValueError, TypeError):
            results = []
    n_correct = sum(1 for r in results if r.get("ok"))
    return render_template("history_detail.html", a=a, results=results,
                           n_correct=n_correct)


@app.template_filter("modename")
def modename(m):
    for lk, _, folders in questions.CONTENT_TREE:
        for fk, fname in folders:
            if fk == m:
                return fname
    return {"hs_gioi": "Đề HS Giỏi", "olympic": "Đề Thi Olympic",
            "mixed": "HS Giỏi + Thi Olympic", "bao_meo": "Bảo Mèo"}.get(m, m)


# ── MarkItDown routes ──────────────────────────────────────────────────────────

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        return render_template("upload.html")

    f = request.files.get("file")
    if not f or not f.filename:
        flash("Vui lòng chọn file.")
        return render_template("upload.html"), 400

    ext = os.path.splitext(f.filename)[1].lower()
    if ext not in _ALLOWED_EXTS:
        flash(f"Định dạng '{ext}' không được hỗ trợ. Chấp nhận: {', '.join(sorted(_ALLOWED_EXTS))}")
        return render_template("upload.html"), 400

    data = f.read()
    if len(data) > _UPLOAD_MAX_BYTES:
        flash("File vượt quá giới hạn 25 MB.")
        return render_template("upload.html"), 400

    try:
        result = md_client.from_file(f.filename, data, f.content_type)
    except MarkItDownError as exc:
        flash(f"Lỗi convert: {exc}")
        return render_template("upload.html"), 502

    title = result.get("title") or os.path.splitext(f.filename)[0]
    conn = get_db()
    doc_id = _save_document(conn, title, f"upload:{f.filename}", result["markdown"])
    conn.close()
    return redirect(url_for("doc_view", doc_id=doc_id))


@app.route("/crawl", methods=["GET", "POST"])
def crawl():
    if request.method == "GET":
        return render_template("crawl.html")

    url = request.form.get("url", "").strip()
    if not url:
        flash("Vui lòng nhập URL.")
        return render_template("crawl.html"), 400

    try:
        url = _validate_crawl_url(url)
    except ValueError as exc:
        flash(str(exc))
        return render_template("crawl.html"), 400

    try:
        result = md_client.from_url(url)
    except MarkItDownError as exc:
        flash(f"Lỗi convert: {exc}")
        return render_template("crawl.html"), 502

    title = result.get("title") or url
    conn = get_db()
    doc_id = _save_document(conn, title, url, result["markdown"])
    conn.close()
    return redirect(url_for("doc_view", doc_id=doc_id))


@app.route("/doc/<int:doc_id>")
def doc_view(doc_id):
    conn = get_db()
    row = conn.execute(
        _ph("SELECT * FROM documents WHERE id = ?"), (doc_id,)
    ).fetchone()
    conn.close()
    if row is None:
        return render_template("doc.html", doc=None, html_content=""), 404
    doc = dict(row)
    html_content = md_lib.markdown(
        doc["markdown"],
        extensions=["tables", "fenced_code", "nl2br", "sane_lists"],
    )
    return render_template("doc.html", doc=doc, html_content=html_content)


@app.route("/docs")
def docs_list():
    conn = get_db()
    rows = conn.execute(
        "SELECT id, title, source, created_at FROM documents ORDER BY created_at DESC LIMIT 100"
    ).fetchall()
    conn.close()
    return render_template("docs_list.html", docs=[dict(r) for r in rows])


@app.route("/admin/crawl-report")
def crawl_report():
    conn = get_db()
    try:
        rows = conn.execute("""
            SELECT date(created_at) as day,
                   grade, subject, folder_type,
                   COUNT(*) as total_urls,
                   COALESCE(SUM(questions_extracted), 0) as total_q,
                   SUM(CASE WHEN status='success'  THEN 1 ELSE 0 END) as ok,
                   SUM(CASE WHEN status='failed'   THEN 1 ELSE 0 END) as fail
            FROM crawl_log
            WHERE created_at >= date('now', '-14 days')
            GROUP BY day, grade, subject, folder_type
            ORDER BY day DESC, grade, subject
        """).fetchall()
    except Exception:
        rows = []
    conn.close()
    # Nhóm theo ngày
    by_day = {}
    for r in rows:
        d = r["day"]
        by_day.setdefault(d, []).append(dict(r))
    return render_template("crawl_report.html", by_day=by_day)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
