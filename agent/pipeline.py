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
    PHASE1_POOL_TARGET, REQUEST_TIMEOUT, WEEKLY_TARGET_PER_CATEGORY,
)
from agent.crawler import download_file, file_hash, find_file_urls
from agent.db import (
    count_today, count_total, init_agent_tables, is_url_crawled, log_crawl,
    save_questions,
)
from agent.extractor import extract_questions

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)


# ── MarkItDown local (pip install markitdown) — không cần server/API key ──────

def _convert_to_markdown(filename: str, data: bytes, content_type: str) -> str | None:
    try:
        import tempfile, os
        from markitdown import MarkItDown
        # Ghi tạm ra file vì markitdown cần đường dẫn
        suffix = os.path.splitext(filename)[1] or ".pdf"
        with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
            tmp.write(data)
            tmp_path = tmp.name
        try:
            md = MarkItDown()
            result = md.convert(tmp_path)
            return result.text_content or ""
        finally:
            os.unlink(tmp_path)
    except Exception as exc:
        log.warning("MarkItDown convert failed (%s): %s", filename, exc)
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

def _effective_target(grade: str, subject: str, folder_type: str) -> int:
    """Phase 1 (pool < PHASE1_POOL_TARGET): 1/ngày.
    Phase 2 (pool đủ rồi): 3/tuần → chỉ chạy thứ 2/4/6, ngày khác target=0."""
    from datetime import date
    total = count_total(grade, subject, folder_type)
    if total < PHASE1_POOL_TARGET:
        return DAILY_TARGET_PER_CATEGORY   # phase 1: 1/ngày

    # Phase 2: 3 đề/tuần — chạy vào thứ 2, 4, 6 (weekday 0, 2, 4)
    weekday = date.today().weekday()
    if weekday in (0, 2, 4):
        return 1   # mỗi ngày chạy 1 đề, 3 lần/tuần = 3/tuần
    return 0       # ngày còn lại bỏ qua


def run_all():
    init_agent_tables()
    log.info("=== Agent bắt đầu (free mode — regex only) ===")
    total_added = 0
    for grade, subject, folder_type, keyword in CATEGORIES:
        try:
            target = _effective_target(grade, subject, folder_type)
            if target == 0:
                log.info("[%s/%s/%s] Phase 2 — hôm nay nghỉ", grade, subject, folder_type)
                continue
            phase = 1 if count_total(grade, subject, folder_type) < PHASE1_POOL_TARGET else 2
            log.info("[%s/%s/%s] Phase %d — target %d", grade, subject, folder_type, phase, target)
            n = run_category(grade, subject, folder_type, keyword, target)
            total_added += n
        except Exception as exc:
            log.error("[%s/%s/%s] Lỗi: %s", grade, subject, folder_type, exc)
    log.info("=== Xong. Tổng đề mới hôm nay: %d ===", total_added)
    return total_added


if __name__ == "__main__":
    run_all()
