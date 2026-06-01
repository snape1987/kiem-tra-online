"""Client cho MarkItDown microservice.

Đọc 2 env var:
  MARKITDOWN_URL     — base URL của service (vd. https://mark.suong.io)
  MARKITDOWN_API_KEY — API key, gửi qua header X-Api-Key

Raise MarkItDownError khi service trả về HTTP non-200.
"""
import mimetypes
import os

import requests

_BASE_URL = os.environ.get("MARKITDOWN_URL", "").rstrip("/")
_API_KEY  = os.environ.get("MARKITDOWN_API_KEY", "")
_TIMEOUT  = 120   # giây — khớp với spec service


class MarkItDownError(Exception):
    """Lỗi từ MarkItDown service (HTTP non-200 hoặc service chưa cấu hình)."""


def _require_config():
    if not _BASE_URL:
        raise MarkItDownError(
            "MARKITDOWN_URL chưa được set. "
            "Thêm env var MARKITDOWN_URL vào DigitalOcean App Settings."
        )


def _headers() -> dict:
    return {"X-Api-Key": _API_KEY} if _API_KEY else {}


def from_url(url: str) -> dict:
    """Chuyển một URL thành markdown.

    Args:
        url: URL công khai cần convert.

    Returns:
        dict với keys: markdown (str), title (str), metadata (dict).

    Raises:
        MarkItDownError: khi service trả về lỗi.
    """
    _require_config()
    resp = requests.post(
        f"{_BASE_URL}/convert/url",
        json={"url": url},
        headers=_headers(),
        timeout=_TIMEOUT,
    )
    if not resp.ok:
        raise MarkItDownError(
            f"MarkItDown /convert/url lỗi HTTP {resp.status_code}: "
            f"{resp.text[:300]}"
        )
    return resp.json()


def from_file(filename: str, data: bytes, content_type: str | None = None) -> dict:
    """Chuyển file binary thành markdown.

    Args:
        filename:     Tên file gốc (vd. "bai-hoc.pdf").
        data:         Nội dung file dạng bytes.
        content_type: MIME type; tự đoán từ filename nếu None.

    Returns:
        dict với keys: markdown (str), title (str), metadata (dict).

    Raises:
        MarkItDownError: khi service trả về lỗi.
    """
    _require_config()
    if content_type is None:
        guessed, _ = mimetypes.guess_type(filename)
        content_type = guessed or "application/octet-stream"
    resp = requests.post(
        f"{_BASE_URL}/convert/file",
        files={"file": (filename, data, content_type)},
        headers=_headers(),
        timeout=_TIMEOUT,
    )
    if not resp.ok:
        raise MarkItDownError(
            f"MarkItDown /convert/file lỗi HTTP {resp.status_code}: "
            f"{resp.text[:300]}"
        )
    return resp.json()


def from_path(path: str) -> dict:
    """Đọc file từ đường dẫn cục bộ rồi convert.

    Args:
        path: Đường dẫn tuyệt đối hoặc tương đối đến file.

    Returns:
        dict với keys: markdown (str), title (str), metadata (dict).
    """
    filename = os.path.basename(path)
    with open(path, "rb") as fh:
        data = fh.read()
    return from_file(filename, data)
