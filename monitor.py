# =========================================
# CodeSandbox Keep-Alive Monitor
# =========================================
# Install:
# pip install requests schedule
#
# Run:
# python monitor.py
#
# This script:
# ✅ Pings your CodeSandbox every few minutes
# ✅ Keeps it active
# ✅ Auto restarts monitoring if error
# ✅ Logs status
#
# Replace YOUR_CODESANDBOX_URL with your sandbox URL
# Example:
# https://abcd1234.csb.app
# =========================================

import requests
import time
import schedule
from datetime import datetime

# =========================
# SETTINGS
# =========================

SANDBOX_URL = "https://YOUR_CODESANDBOX_URL.csb.app"

PING_INTERVAL_MINUTES = 5

# Optional:
# Add more endpoints if needed
URLS = [
    SANDBOX_URL,
]

# =========================
# FUNCTIONS
# =========================

def log(msg):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] {msg}")

def ping_site(url):
    try:
        response = requests.get(url, timeout=15)

        if response.status_code == 200:
            log(f"ONLINE ✅ {url}")
        else:
            log(f"STATUS {response.status_code} ⚠️ {url}")

    except Exception as e:
        log(f"OFFLINE ❌ {url}")
        log(str(e))

def monitor():
    log("Running monitor...")

    for url in URLS:
        ping_site(url)

# =========================
# START
# =========================

log("CodeSandbox Monitor Started 🚀")

monitor()

schedule.every(PING_INTERVAL_MINUTES).minutes.do(monitor)

while True:
    try:
        schedule.run_pending()
        time.sleep(1)

    except Exception as e:
        log(f"MAIN LOOP ERROR: {e}")
        time.sleep(10)
