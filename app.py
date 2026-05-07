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


def get_theme(student_key):
    return STUDENT_THEMES.get(student_key, STUDENT_THEMES["bao_meo"])


@app.route("/")
def index():
    content_tree_json = json.dumps([
        {"key": lk, "display": ld,
         "folders": [{"key": fk, "display": fd} for fk, fd in folders]}
        for lk, ld, folders in questions.CONTENT_TREE
    ])
    return render_template("index.html", themes=STUDENT_THEMES, content_tree_json=content_tree_json)


@app.route("/start", methods=["POST"])
def start():
    student_key = request.form.get("student_key", "bao_meo")
    theme = get_theme(student_key)
    student = theme["name"]
    lop = request.form.get("lop", "lop_1")
    folder = request.form.get("folder", "de_hk2_toan_1")
    duration = int(request.form.get("duration", 45))
    n_q = int(request.form.get("n_questions", DUR_TO_NQ.get(duration, 15)))

    seed = int(time.time() * 1000) % 1_000_000
    qs = questions.gen_exam(lop, folder, n=n_q, seed=seed)

    session["student"] = student
    session["student_key"] = student_key
    session["lop"] = lop
    session["folder"] = folder
    session["duration"] = duration
    session["questions"] = qs
    session["start_time"] = time.time()
    return redirect(url_for("exam"))


@app.route("/exam")
def exam():
    qs = session.get("questions")
    if not qs:
        return redirect(url_for("index"))
    student_key = session.get("student_key", "bao_meo")
    theme = get_theme(student_key)
    icons = load_icons_multi(theme["icon_dirs"])
    random.shuffle(icons)
    lop = session.get("lop", "lop_1")
    folder = session.get("folder", "de_hk2_toan_1")
    return render_template(
        "exam.html",
        questions=qs,
        duration=session.get("duration", 45),
        student=session.get("student", "Bé"),
        student_key=student_key,
        folder_name=questions.folder_display(lop, folder),
        theme=theme,
        icons=icons,
        audio_file="",
    )


@app.route("/submit", methods=["POST"])
def submit():
    qs = session.get("questions")
    if not qs:
        return redirect(url_for("index"))

    student = session.get("student", "Bé")
    student_key = session.get("student_key", "bao_meo")
    theme = get_theme(student_key)
    lop = session.get("lop", "lop_1")
    folder = session.get("folder", "de_hk2_toan_1")
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
                         "explanation": q.get("explanation", "")})

    total = len(qs)
    score_10 = round(score * 10 / total) if total else 0

    conn = get_db()
    conn.execute(
        "INSERT INTO attempts (student, student_key, mode, duration, score, total, time_used, created_at)"
        " VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (student, student_key, folder, duration, score_10, total, time_used,
         datetime.now().isoformat(timespec="seconds")),
    )
    conn.commit()
    conn.close()

    all_icons = load_icons_multi(theme["icon_dirs"])
    session.pop("questions", None)
    return render_template(
        "result.html",
        student=student, student_key=student_key,
        folder_name=questions.folder_display(lop, folder), theme=theme,
        score=score_10, raw_score=score, total=total,
        time_used=time_used, results=results,
        icons_json=json.dumps(all_icons),
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
