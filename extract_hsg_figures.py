"""
extract_hsg_figures.py — One-off script to extract geometry figures from HSG PDF files.

Requires:
    pip install pymupdf

Usage:
    1. Download the 4 PDFs from Google Drive and save locally (or provide paths).
    2. Update PDF_PATHS dict below with local file paths.
    3. Run: python extract_hsg_figures.py

Output: saves PNG files to static/hsg_figures/
"""

import os
import fitz  # PyMuPDF

OUT_DIR = os.path.join(os.path.dirname(__file__), "static", "hsg_figures")
os.makedirs(OUT_DIR, exist_ok=True)

# ── Configure: set local PDF paths before running ──────────────────────────
PDF_PATHS = {
    "nhu_thanh":    r"path\to\xa-nhu-thanh.pdf",      # Drive ID: 1J6dDMK6WOSecrmrwpfGuaSBe5Kd-NBvj
    "ba_thuoc":     r"path\to\xa-ba-thuoc.pdf",        # Drive ID: 1aFDr... (check Drive)
    "quang_ngoc":   r"path\to\xa-quang-ngoc.pdf",      # volleyball court
    "tong_son":     r"path\to\xa-tong-son.pdf",        # Drive ID: composite trapezoids
}

# ── Figure specs: (pdf_key, page_index_0based, crop_rect or None for full page) ──
# crop_rect = fitz.Rect(x0, y0, x1, y1) in points (72 points = 1 inch)
# Set to None to render the full page; adjust after inspecting the PDF.
FIGURES = [
    {
        "pdf":    "nhu_thanh",
        "page":   0,          # adjust to the page containing the garden figure (Câu 7)
        "crop":   None,       # fitz.Rect(50, 400, 500, 700) — adjust after inspection
        "out":    "nhu_thanh_c7.png",
        "desc":   "Vườn hình chữ nhật với lối đi hình bình hành (xa-nhu-thanh Câu 7)",
    },
    {
        "pdf":    "ba_thuoc",
        "page":   1,          # adjust to the page containing the trapezoid figure (Câu 9.2)
        "crop":   None,
        "out":    "ba_thuoc_c9.png",
        "desc":   "Hình thang ABEF trong hình chữ nhật 16x10m (xa-ba-thuoc Câu 9.2)",
    },
    {
        "pdf":    "quang_ngoc",
        "page":   0,          # adjust to volleyball court diagram page (Câu 7b)
        "crop":   None,
        "out":    "volleyball_court.png",
        "desc":   "Sân bóng chuyền với vạch sơn 5cm (xa-quang-ngoc Câu 7b)",
    },
    {
        "pdf":    "tong_son",
        "page":   1,          # adjust to composite trapezoid figure (Câu IV.2)
        "crop":   None,
        "out":    "tong_son_cIV.png",
        "desc":   "Hình thang ghép ABCF+CDEF (xa-tong-son Câu IV.2)",
    },
]

DPI = 150  # render resolution (150 DPI is clear enough for screen display)


def extract_figure(spec: dict) -> None:
    pdf_path = PDF_PATHS.get(spec["pdf"])
    if not pdf_path or not os.path.isfile(pdf_path):
        print(f"  [SKIP] {spec['out']}: PDF not found at {pdf_path!r}")
        return

    doc = fitz.open(pdf_path)
    page_idx = spec["page"]
    if page_idx >= len(doc):
        print(f"  [SKIP] {spec['out']}: page {page_idx} out of range (doc has {len(doc)} pages)")
        doc.close()
        return

    page = doc[page_idx]
    zoom = DPI / 72
    mat = fitz.Matrix(zoom, zoom)

    if spec["crop"]:
        clip = spec["crop"]
        pix = page.get_pixmap(matrix=mat, clip=clip)
    else:
        pix = page.get_pixmap(matrix=mat)

    out_path = os.path.join(OUT_DIR, spec["out"])
    pix.save(out_path)
    doc.close()
    print(f"  [OK]   {spec['out']} → {out_path}  ({pix.width}×{pix.height} px)")


if __name__ == "__main__":
    print(f"Extracting {len(FIGURES)} figures to {OUT_DIR}")
    for spec in FIGURES:
        print(f"\n{spec['desc']}")
        extract_figure(spec)
    print("\nDone. Review each PNG and adjust 'crop' rects if needed.")
    print("After placing PNGs in static/hsg_figures/, restart Flask to serve them.")
