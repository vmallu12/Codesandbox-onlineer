import requests
import time
from datetime import datetime

# =====================================
# YOUR CODESANDBOX URL
# =====================================

URLS = [
    "https://YOUR-SANDBOX.csb.app"
]

# Ping every 60 sec
PING_DELAY = 60


def log(text):
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] {text}")


def ping(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Cache-Control": "no-cache"
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
        log(f"ERROR ❌ {url}")
        log(str(e))


print("🚀 CodeSandbox Keep Alive Started")

while True:
    try:
        for url in URLS:
            ping(url)

        time.sleep(PING_DELAY)

    except Exception as e:
        print("MAIN LOOP ERROR:", e)
        time.sleep(10)
