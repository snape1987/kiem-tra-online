"""Flask webapp — Kiểm Tra Online — Gia Đình SU KHÔI MÈO."""
import os
import random
import sqlite3
import time
import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session

import questions

app = Flask(__name__)
app.secret_key = "kiemtra-sukhoikem-2026"
_DATA_DIR = os.environ.get("DATA_DIR", os.path.dirname(__file__))
DB_PATH = os.path.join(_DATA_DIR, "kiemtra.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
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
    conn.execute("""
        CREATE TABLE IF NOT EXISTS exam_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_key TEXT NOT NULL,
            folder TEXT NOT NULL,
            exam_no INTEGER NOT NULL,
            score INTEGER,
            completed_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


init_db()

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
}

DUR_TO_NQ = {45: 15, 60: 20, 90: 30}

FOLDER_EXAM_COUNTS = {
    # Lớp 1
    "de_hk2_toan_1":       1,   # 1 PDF đề HK2
    "toan_violympic_1":   19,   # 3 PDF cùng nội dung → 19 vòng
    # Lớp 6
    "de_toan_6_hk2":       9,   # 9 PDF đề đơn
    "de_olympic_toan_6":  29,   # 10 đề đơn + VIOLYMPIC TOÁN 6 có 19 vòng
    "de_hsg_toan_6":      11,   # 11 PDF đề HSG cấp trường/xã
    "de_hsg_anh_6":        36,   # 36 đề HSG Anh 6 (mỗi đề có file MP3)
    "de_tieng_anh_6_hk2": 10,   # 5 đề Lớp 6 + 5 đề Lớp 8
    # Lớp 7
    "toan_7_hk1":         14,   # 14 PDF đề đơn
    "tieng_anh_7_hk1":    29,   # 29 PDF đề đơn
    # Lớp 8
    "toan_8_hk2":         16,   # 6 PDF + 10 docx đề đơn
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
        "SELECT student_key, folder, exam_no FROM exam_progress"
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
        audio_file = f"hsg_anh_6/de_{exam_no:02d}.mp3"
        audio_label = "A. LISTENING — Nhấn ▶ để nghe. Được nghe lại 2 lần."
        subject = "Tiếng Anh"
    else:
        audio_file = ""
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
        audio_file=audio_file,
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
    for i, q in enumerate(qs):
        user_ans = request.form.get(f"q_{i}", "").strip()
        correct = str(q["answer"]).strip()
        ok = user_ans.lower().replace(" ", "") == correct.lower().replace(" ", "")
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
        "INSERT INTO attempts (student, student_key, mode, duration, score, total, time_used, created_at)"
        " VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (student, student_key, folder, duration, score_10, total, time_used,
         datetime.now().isoformat(timespec="seconds")),
    )
    conn.execute(
        "INSERT INTO exam_progress (student_key, folder, exam_no, score, completed_at)"
        " VALUES (?, ?, ?, ?, ?)",
        (student_key, folder, exam_no, score_10,
         datetime.now().isoformat(timespec="seconds")),
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


@app.template_filter("modename")
def modename(m):
    for lk, _, folders in questions.CONTENT_TREE:
        for fk, fname in folders:
            if fk == m:
                return fname
    return {"hs_gioi": "Đề HS Giỏi", "olympic": "Đề Thi Olympic",
            "mixed": "HS Giỏi + Thi Olympic", "bao_meo": "Bảo Mèo"}.get(m, m)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
