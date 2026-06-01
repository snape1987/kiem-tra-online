"""Scheduler: chạy pipeline hàng ngày lúc 2 giờ sáng.

Deploy trên hermes droplet:
    # Cài dependencies
    pip install -r requirements_agent.txt

    # Chạy daemon (nohup để không tắt khi logout)
    nohup python -m agent.scheduler >> /var/log/kiem-tra-agent.log 2>&1 &

    # Hoặc dùng cron (thêm vào crontab):
    # 0 2 * * * cd /path/to/app && python -m agent.pipeline >> /var/log/kiem-tra-agent.log 2>&1
"""
import logging
import sys
import time
from datetime import datetime, timedelta

from agent.pipeline import run_all

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [SCHEDULER] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)

DAILY_RUN_HOUR = 2   # 2:00 AM


def _next_run_time() -> datetime:
    now  = datetime.now()
    next_run = now.replace(hour=DAILY_RUN_HOUR, minute=0, second=0, microsecond=0)
    if next_run <= now:
        next_run += timedelta(days=1)
    return next_run


def run_daemon():
    log.info("Scheduler khởi động — chạy lúc %02d:00 mỗi ngày", DAILY_RUN_HOUR)
    while True:
        next_run = _next_run_time()
        wait_sec = (next_run - datetime.now()).total_seconds()
        log.info("Lần chạy tiếp theo: %s (còn %.0f giây)", next_run, wait_sec)
        time.sleep(max(wait_sec, 1))
        log.info("--- Bắt đầu chạy hàng ngày ---")
        try:
            run_all()
        except Exception as exc:
            log.error("Pipeline lỗi: %s", exc)


if __name__ == "__main__":
    # Nếu truyền --now thì chạy ngay 1 lần rồi thoát
    if "--now" in sys.argv:
        run_all()
    else:
        run_daemon()
