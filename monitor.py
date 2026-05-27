import requests
import time
from datetime import datetime

# =========================
# YOUR CODESANDBOX URL
# =========================

URLS = [
    "https://YOUR-SANDBOX.csb.app"
]

# Ping every 300 sec (5 min)
PING_DELAY = 300


def log(text):
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] {text}")


def ping(url):
    try:
        r = requests.get(url, timeout=20)

        if r.status_code == 200:
            log(f"ONLINE ✅ {url}")

        else:
            log(f"STATUS {r.status_code} ⚠️ {url}")

    except Exception as e:
        log(f"OFFLINE ❌ {url}")
        log(str(e))


log("Monitor Started 🚀")

while True:
    for url in URLS:
        ping(url)

    time.sleep(PING_DELAY)
