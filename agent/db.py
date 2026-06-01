"""DB helpers cho agent — dùng chung schema với webapp."""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from agent.config import DATABASE_URL, USE_PG, SQLITE_PATH


def get_conn():
    if USE_PG:
        import psycopg
        from psycopg.rows import dict_row
        return psycopg.connect(DATABASE_URL, row_factory=dict_row)
    import sqlite3
    conn = sqlite3.connect(SQLITE_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def ph(sql: str) -> str:
    return sql.replace("?", "%s") if USE_PG else sql


def init_agent_tables():
    """Tạo bảng nếu chưa có — gọi một lần khi agent khởi động."""
    pk = "SERIAL PRIMARY KEY" if USE_PG else "INTEGER PRIMARY KEY AUTOINCREMENT"
    conn = get_conn()

    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS questions_pool (
            id          {pk},
            grade       TEXT NOT NULL,
            subject     TEXT NOT NULL,
            folder_type TEXT NOT NULL,
            q           TEXT NOT NULL,
            options_json TEXT,
            answer      TEXT NOT NULL,
            topic       TEXT,
            source_url  TEXT,
            source_file TEXT,
            confidence  REAL DEFAULT 1.0,
            created_at  TEXT NOT NULL,
            UNIQUE(grade, subject, folder_type, q)
        )
    """)

    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS crawl_log (
            id                  {pk},
            url                 TEXT NOT NULL,
            file_hash           TEXT,
            status              TEXT NOT NULL,
            grade               TEXT,
            subject             TEXT,
            folder_type         TEXT,
            questions_extracted INTEGER DEFAULT 0,
            error_msg           TEXT,
            created_at          TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def count_today(grade: str, subject: str, folder_type: str) -> int:
    """Đếm số đề đã thêm hôm nay cho một mục."""
    from datetime import date
    today = date.today().isoformat()
    conn = get_conn()
    row = conn.execute(
        ph("SELECT COUNT(DISTINCT source_file) as n FROM questions_pool "
           "WHERE grade=? AND subject=? AND folder_type=? AND created_at >= ?"),
        (grade, subject, folder_type, today),
    ).fetchone()
    conn.close()
    return (row["n"] or 0) if row else 0


def count_total(grade: str, subject: str, folder_type: str) -> int:
    """Đếm tổng số đề trong pool cho một mục."""
    conn = get_conn()
    row = conn.execute(
        ph("SELECT COUNT(DISTINCT source_file) as n FROM questions_pool "
           "WHERE grade=? AND subject=? AND folder_type=?"),
        (grade, subject, folder_type),
    ).fetchone()
    conn.close()
    return (row["n"] or 0) if row else 0


def is_url_crawled(url: str) -> bool:
    """Kiểm tra URL đã crawl thành công chưa."""
    conn = get_conn()
    row = conn.execute(
        ph("SELECT id FROM crawl_log WHERE url=? AND status='success' LIMIT 1"),
        (url,),
    ).fetchone()
    conn.close()
    return row is not None


def save_questions(questions: list[dict], grade: str, subject: str,
                   folder_type: str, source_url: str, source_file: str) -> int:
    """Lưu danh sách câu hỏi vào pool, trả về số câu lưu được."""
    from datetime import datetime
    now = datetime.now().isoformat(timespec="seconds")
    conn = get_conn()
    saved = 0
    for q in questions:
        try:
            conn.execute(
                ph("INSERT OR IGNORE INTO questions_pool "
                   "(grade, subject, folder_type, q, options_json, answer, "
                   " topic, source_url, source_file, confidence, created_at) "
                   "VALUES (?,?,?,?,?,?,?,?,?,?,?)"),
                (
                    grade, subject, folder_type,
                    q["q"],
                    json.dumps(q.get("options"), ensure_ascii=False) if q.get("options") else None,
                    q["answer"],
                    q.get("topic", ""),
                    source_url,
                    source_file,
                    q.get("confidence", 1.0),
                    now,
                ),
            )
            saved += 1
        except Exception:
            pass   # duplicate hoặc lỗi constraint — bỏ qua
    conn.commit()
    conn.close()
    return saved


def log_crawl(url: str, file_hash: str | None, status: str,
              grade: str | None, subject: str | None, folder_type: str | None,
              questions_extracted: int = 0, error_msg: str | None = None):
    from datetime import datetime
    now = datetime.now().isoformat(timespec="seconds")
    conn = get_conn()
    conn.execute(
        ph("INSERT INTO crawl_log "
           "(url, file_hash, status, grade, subject, folder_type, "
           " questions_extracted, error_msg, created_at) "
           "VALUES (?,?,?,?,?,?,?,?,?)"),
        (url, file_hash, status, grade, subject, folder_type,
         questions_extracted, error_msg, now),
    )
    conn.commit()
    conn.close()


def get_pool_questions(grade: str, subject: str, folder_type: str) -> list[dict]:
    """Lấy toàn bộ câu hỏi từ pool cho gen_exam."""
    conn = get_conn()
    rows = conn.execute(
        ph("SELECT q, options_json, answer, topic FROM questions_pool "
           "WHERE grade=? AND subject=? AND folder_type=?"),
        (grade, subject, folder_type),
    ).fetchall()
    conn.close()
    result = []
    for r in rows:
        item = {
            "type": "choice" if r["options_json"] else "fill",
            "q": r["q"],
            "answer": r["answer"],
            "topic": r["topic"] or "",
        }
        if r["options_json"]:
            item["options"] = json.loads(r["options_json"])
        result.append(item)
    return result
