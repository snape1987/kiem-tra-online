"""Cấu hình agent crawl đề thi."""
import os

# ── Database (dùng chung với webapp) ─────────────────────────────────────────
DATABASE_URL = os.environ.get("DATABASE_URL", "").strip()
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = "postgresql://" + DATABASE_URL[len("postgres://"):]
USE_PG = DATABASE_URL.startswith("postgresql://")
SQLITE_PATH = os.environ.get(
    "SQLITE_PATH",
    os.path.join(os.path.dirname(__file__), "..", "kiemtra.db"),
)

# ── Claude API — tắt để miễn phí, chỉ dùng regex extractor ─────────────────
ANTHROPIC_API_KEY = ""   # để trống = không gọi Claude API
CLAUDE_MODEL      = "claude-3-5-haiku-20241022"

# ── MarkItDown service ────────────────────────────────────────────────────────
MARKITDOWN_URL     = os.environ.get("MARKITDOWN_URL", "").rstrip("/")
MARKITDOWN_API_KEY = os.environ.get("MARKITDOWN_API_KEY", "")

# ── Serper.dev Google Search API (2500 queries/tháng free, không cần billing) ─
SERPER_API_KEY = os.environ.get("SERPER_API_KEY", "")

# ── Mục tiêu ─────────────────────────────────────────────────────────────────
# Phase 1 (đang dùng): 1 đề mới/ngày/mục cho đến khi đủ PHASE1_POOL_TARGET
# Phase 2 (tự động chuyển): 3 đề/tuần/mục để duy trì
DAILY_TARGET_PER_CATEGORY = 1
PHASE1_POOL_TARGET        = 20   # đủ 20 đề/mục → chuyển sang chế độ tuần
WEEKLY_TARGET_PER_CATEGORY = 3

# ── Danh mục cần crawl ───────────────────────────────────────────────────────
# (grade, subject, folder_type, search_keywords_vi)
CATEGORIES = [
    # Lớp 1
    ("lop_1", "toan",      "hk2",      "đề kiểm tra toán lớp 1 học kỳ 2"),
    ("lop_1", "toan",      "hsg",      "đề thi học sinh giỏi toán lớp 1"),
    ("lop_1", "toan",      "violympic","đề thi violympic toán lớp 1"),
    # Lớp 2
    ("lop_2", "toan",      "hk1",      "đề kiểm tra toán lớp 2 học kỳ 1"),
    ("lop_2", "toan",      "hk2",      "đề kiểm tra toán lớp 2 học kỳ 2"),
    ("lop_2", "toan",      "hsg",      "đề thi học sinh giỏi toán lớp 2"),
    ("lop_2", "toan",      "violympic","đề thi violympic toán lớp 2"),
    ("lop_2", "tieng_anh", "hk1",      "đề kiểm tra tiếng anh lớp 2 học kỳ 1 trắc nghiệm"),
    ("lop_2", "tieng_anh", "hk2",      "đề kiểm tra tiếng anh lớp 2 học kỳ 2 trắc nghiệm"),
    # Lớp 6
    ("lop_6", "toan",      "hk1",      "đề kiểm tra toán lớp 6 học kỳ 1"),
    ("lop_6", "toan",      "hk2",      "đề kiểm tra toán lớp 6 học kỳ 2"),
    ("lop_6", "toan",      "hsg",      "đề thi học sinh giỏi toán lớp 6"),
    ("lop_6", "toan",      "violympic","đề thi violympic toán lớp 6"),
    ("lop_6", "tieng_anh", "hk1",      "đề thi tiếng anh lớp 6 học kỳ 1 trắc nghiệm đáp án"),
    ("lop_6", "tieng_anh", "hk2",      "đề thi tiếng anh lớp 6 học kỳ 2 trắc nghiệm đáp án"),
    ("lop_6", "tieng_anh", "hsg",      "đề thi học sinh giỏi tiếng anh lớp 6 có đáp án"),
    # Lớp 7
    ("lop_7", "toan",      "hk1",      "đề kiểm tra toán lớp 7 học kỳ 1"),
    ("lop_7", "toan",      "hk2",      "đề kiểm tra toán lớp 7 học kỳ 2"),
    ("lop_7", "toan",      "hsg",      "đề thi học sinh giỏi toán lớp 7"),
    ("lop_7", "tieng_anh", "hk1",      "đề thi tiếng anh lớp 7 học kỳ 1 trắc nghiệm đáp án"),
    ("lop_7", "tieng_anh", "hk2",      "đề thi tiếng anh lớp 7 học kỳ 2 trắc nghiệm đáp án"),
    ("lop_7", "tieng_anh", "hsg",      "đề thi học sinh giỏi tiếng anh lớp 7 có đáp án"),
    # Lớp 8
    ("lop_8", "toan",      "hk1",      "đề kiểm tra toán lớp 8 học kỳ 1"),
    ("lop_8", "toan",      "hk2",      "đề kiểm tra toán lớp 8 học kỳ 2"),
    ("lop_8", "toan",      "hsg",      "đề thi học sinh giỏi toán lớp 8"),
    ("lop_8", "tieng_anh", "hk1",      "đề thi tiếng anh lớp 8 học kỳ 1 trắc nghiệm đáp án"),
    ("lop_8", "tieng_anh", "hk2",      "đề thi tiếng anh lớp 8 học kỳ 2 trắc nghiệm đáp án"),
    ("lop_8", "tieng_anh", "hsg",      "đề thi học sinh giỏi tiếng anh lớp 8 có đáp án"),
]

# ── Số câu mỗi đề theo loại ──────────────────────────────────────────────────
NQ_BY_TYPE = {
    "hk1":       20,
    "hk2":       20,
    "hsg":       30,
    "violympic": 30,
}

# ── Nguồn crawl ──────────────────────────────────────────────────────────────
CRAWL_SOURCES = [
    "https://vndoc.com",
    "https://tailieu.vn",
    "https://violet.vn",
    "https://toanhoc247.com",
    "https://hocmai.vn",
]

# ── Giới hạn ─────────────────────────────────────────────────────────────────
MAX_FILE_BYTES    = 20 * 1024 * 1024   # 20 MB
REQUEST_TIMEOUT   = 30                 # giây
CRAWL_DELAY       = 2                  # giây giữa các request (lịch sự với server)
MAX_URLS_PER_CAT  = 20                 # số URL tối đa duyệt mỗi mục mỗi lần chạy
