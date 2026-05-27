# =========================================
# CodeSandbox Keep Alive Monitor
# Railway Ready
# =========================================

import requests
import time
from datetime import datetime

# =========================================
# YOUR CODESANDBOX URL
# Replace with your real sandbox URL
# =========================================

URLS = [
    "https://YOUR-SANDBOX.csb.app"
]

# Ping delay in seconds
PING_DELAY = 300  # 5 minutes


# =========================================
# LOG FUNCTION
# =========================================

def log(text):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] {text}")


# =========================================
# PING FUNCTION
# =========================================

def ping(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        r = requests.get(
            url,
            headers=headers,
            timeout=20
        )

        if r.status_code == 200:
            log(f"ONLINE ✅ {url}")

        else:
            log(f"STATUS {r.status_code} ⚠️ {url}")

    except Exception as e:
        log(f"OFFLINE ❌ {url}")
        log(str(e))


# =========================================
# START
# =========================================

log("CodeSandbox Monitor Started 🚀")

while True:
    try:
        for url in URLS:
            ping(url)

        time.sleep(PING_DELAY)

    except Exception as e:
        log(f"MAIN LOOP ERROR ❌ {e}")
        time.sleep(10)
