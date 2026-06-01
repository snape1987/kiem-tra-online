"""Pipeline chính: crawl → convert → extract → lưu DB.

Chạy thủ công:  python -m agent.pipeline
Chạy daemon:    python -m agent.scheduler
"""
import logging
import sys
import time

import requests

from agent.config import (
    CATEGORIES, DAILY_TARGET_PER_CATEGORY, MARKITDOWN_API_KEY, MARKITDOWN_URL,
    REQUEST_TIMEOUT,
)
from agent.crawler import download_file, file_hash, find_file_urls
from agent.db import (
    count_today, init_agent_tables, is_url_crawled, log_crawl, save_questions,
)
from agent.extractor import extract_questions

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)


# ── MarkItDown helper (gọi trực tiếp, không import markitdown_client để
#    agent có thể chạy độc lập với webapp) ─────────────────────────────────────

def _convert_to_markdown(filename: str, data: bytes, content_type: str) -> str | None:
    if not MARKITDOWN_URL:
        log.warning("MARKITDOWN_URL chưa set — bỏ qua convert")
        return None
    headers = {"X-Api-Key": MARKITDOWN_API_KEY} if MARKITDOWN_API_KEY else {}
    try:
        resp = requests.post(
            f"{MARKITDOWN_URL}/convert/file",
            files={"file": (filename, data, content_type)},
            headers=headers,
            timeout=120,
        )
        if not resp.ok:
            log.warning("MarkItDown error %s: %s", resp.status_code, resp.text[:200])
            return None
        return resp.json().get("markdown", "")
    except Exception as exc:
        log.warning("MarkItDown request failed: %s", exc)
        return None


# ── Xử lý một URL ─────────────────────────────────────────────────────────────

def process_url(url: str, grade: str, subject: str, folder_type: str) -> int:
    """Tải, convert, extract rồi lưu. Trả số câu lưu được (0 nếu thất bại)."""
    if is_url_crawled(url):
        return 0

    result = download_file(url)
    if result is None:
        log_crawl(url, None, "failed", grade, subject, folder_type,
                  error_msg="download failed or too large")
        return 0

    data, filename, content_type = result
    fhash = file_hash(data)

    markdown = _convert_to_markdown(filename, data, content_type)
    if not markdown:
        log_crawl(url, fhash, "failed", grade, subject, folder_type,
                  error_msg="markitdown conversion failed")
        return 0

    questions = extract_questions(markdown, folder_type)
    if not questions:
        log_crawl(url, fhash, "no_questions", grade, subject, folder_type)
        return 0

    saved = save_questions(questions, grade, subject, folder_type, url, filename)
    log_crawl(url, fhash, "success", grade, subject, folder_type,
              questions_extracted=saved)
    log.info("  ✓ %s → %d câu lưu được", filename, saved)
    return saved


# ── Xử lý một mục ─────────────────────────────────────────────────────────────

def run_category(grade: str, subject: str, folder_type: str, keyword: str,
                 daily_target: int = DAILY_TARGET_PER_CATEGORY) -> int:
    """Crawl cho đến khi đủ daily_target đề mới hôm nay hoặc hết URL."""
    already_today = count_today(grade, subject, folder_type)
    if already_today >= daily_target:
        log.info("[%s/%s/%s] Đã đủ %d đề hôm nay — bỏ qua",
                 grade, subject, folder_type, already_today)
        return 0

    need = daily_target - already_today
    log.info("[%s/%s/%s] Cần thêm %d đề (đã có hôm nay: %d)",
             grade, subject, folder_type, need, already_today)

    from agent.db import get_conn, ph
    conn = get_conn()
    crawled_urls = set(
        r["url"] for r in conn.execute(
            "SELECT url FROM crawl_log WHERE status='success'"
        ).fetchall()
    )
    conn.close()

    file_urls = find_file_urls(keyword, crawled_urls)
    log.info("  Tìm được %d URL mới để thử", len(file_urls))

    added   = 0
    for url in file_urls:
        if added >= need:
            break
        log.info("  → %s", url[:80])
        n = process_url(url, grade, subject, folder_type)
        if n > 0:
            added += 1
        time.sleep(1)

    return added


# ── Chạy toàn bộ mục ──────────────────────────────────────────────────────────

def run_all(daily_target: int = DAILY_TARGET_PER_CATEGORY):
    init_agent_tables()
    log.info("=== Agent bắt đầu — target %d đề/mục/ngày ===", daily_target)
    total_added = 0
    for grade, subject, folder_type, keyword in CATEGORIES:
        try:
            n = run_category(grade, subject, folder_type, keyword, daily_target)
            total_added += n
        except Exception as exc:
            log.error("[%s/%s/%s] Lỗi: %s", grade, subject, folder_type, exc)
    log.info("=== Xong. Tổng đề mới hôm nay: %d ===", total_added)
    return total_added


if __name__ == "__main__":
    run_all()
