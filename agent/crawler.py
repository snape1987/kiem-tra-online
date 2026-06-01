"""Crawl PDF/DOC từ các trang giáo dục Việt Nam.

Chiến lược:
1. Dùng Google Custom Search hoặc DuckDuckGo scrape để tìm URL tải file.
2. Ưu tiên: vndoc.com, tailieu.vn, violet.vn, toanhoc247.com
3. Tải file về memory (không ghi disk), trả bytes cho pipeline.
"""
import hashlib
import io
import re
import time
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

from agent.config import (
    CRAWL_DELAY, MAX_FILE_BYTES, MAX_URLS_PER_CAT, REQUEST_TIMEOUT,
)

_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0 Safari/537.36"
    ),
    "Accept-Language": "vi-VN,vi;q=0.9,en;q=0.5",
}

_FILE_EXTS = re.compile(r"\.(pdf|docx?|pptx?|xlsx?)(\?.*)?$", re.I)


# ── DuckDuckGo lite search (không cần API key) ────────────────────────────────

def _ddg_search(query: str, num: int = 10) -> list[str]:
    """Tìm URL qua DuckDuckGo HTML — trả danh sách href."""
    try:
        resp = requests.get(
            "https://html.duckduckgo.com/html/",
            params={"q": query, "kl": "vn-vi"},
            headers=_HEADERS,
            timeout=REQUEST_TIMEOUT,
        )
        soup = BeautifulSoup(resp.text, "html.parser")
        links = []
        for a in soup.select("a.result__url"):
            href = a.get("href", "")
            if href.startswith("http"):
                links.append(href)
            if len(links) >= num:
                break
        return links
    except Exception:
        return []


# ── Tìm link tải file trong trang landing ────────────────────────────────────

def _extract_file_links(page_url: str) -> list[str]:
    """Lấy link trực tiếp đến PDF/DOC trong trang."""
    try:
        resp = requests.get(page_url, headers=_HEADERS, timeout=REQUEST_TIMEOUT)
        soup = BeautifulSoup(resp.text, "html.parser")
        base = f"{urlparse(page_url).scheme}://{urlparse(page_url).netloc}"
        links = []
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if _FILE_EXTS.search(href):
                full = href if href.startswith("http") else urljoin(base, href)
                links.append(full)
        return list(dict.fromkeys(links))   # dedup, giữ thứ tự
    except Exception:
        return []


# ── Tải file về memory ────────────────────────────────────────────────────────

def download_file(url: str) -> tuple[bytes, str, str] | None:
    """Tải file, trả (bytes, filename, content_type) hoặc None nếu lỗi/quá lớn."""
    try:
        resp = requests.get(
            url, headers=_HEADERS, timeout=REQUEST_TIMEOUT, stream=True
        )
        if not resp.ok:
            return None
        # Kiểm tra content-length trước khi tải hết
        cl = int(resp.headers.get("content-length", 0))
        if cl and cl > MAX_FILE_BYTES:
            return None

        buf = io.BytesIO()
        size = 0
        for chunk in resp.iter_content(65536):
            buf.write(chunk)
            size += len(chunk)
            if size > MAX_FILE_BYTES:
                return None

        data = buf.getvalue()
        ct   = resp.headers.get("content-type", "application/octet-stream")
        name = url.split("/")[-1].split("?")[0] or "file.pdf"
        return data, name, ct
    except Exception:
        return None


def file_hash(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:16]


# ── Pipeline tìm + tải cho một mục ───────────────────────────────────────────

def find_file_urls(keyword: str, already_crawled: set[str]) -> list[str]:
    """Tìm URL file PDF/DOC chưa được crawl cho keyword.

    Returns list of direct file URLs (không phải landing page).
    """
    file_urls: list[str] = []

    # Tìm trực tiếp file qua DuckDuckGo với filetype hint
    for ftype in ("pdf", "doc"):
        if len(file_urls) >= MAX_URLS_PER_CAT:
            break
        results = _ddg_search(f"{keyword} filetype:{ftype}", num=15)
        time.sleep(CRAWL_DELAY)
        for url in results:
            if url in already_crawled:
                continue
            if _FILE_EXTS.search(url):
                file_urls.append(url)
            else:
                # Trang landing — trích link file trong đó
                sub = _extract_file_links(url)
                time.sleep(CRAWL_DELAY)
                for su in sub:
                    if su not in already_crawled and su not in file_urls:
                        file_urls.append(su)
            if len(file_urls) >= MAX_URLS_PER_CAT:
                break

    return file_urls[:MAX_URLS_PER_CAT]
