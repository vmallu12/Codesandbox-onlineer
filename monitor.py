import requests
import threading
import time
import random
from datetime import datetime

# ==========================================
# YOUR CODESANDBOX URL
# ==========================================

BASE_URL = "https://codesandbox.io/p/devbox/keen-kilby-xktvnf?file=%2Fjishnu"

# ==========================================
# ADVANCED SETTINGS
# ==========================================

PING_INTERVAL = 25
TIMEOUT = 20

ENDPOINTS = [
    "/",
    "/?ping=1",
    "/health",
    "/api",
    "/favicon.ico",
]

USER_AGENTS = [
    "Mozilla/5.0",
    "Chrome/124.0",
    "Safari/537.36",
]

session = requests.Session()

# ==========================================
# LOGGER
# ==========================================

def log(text):
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] {text}")

# ==========================================
# PING FUNCTION
# ==========================================

def keep_alive():
    while True:
        try:
            endpoint = random.choice(ENDPOINTS)

            random_id = random.randint(1000, 999999)

            url = f"{BASE_URL}{endpoint}&_={random_id}"

            headers = {
                "User-Agent": random.choice(USER_AGENTS),
                "Cache-Control": "no-cache",
                "Pragma": "no-cache",
                "Connection": "keep-alive",
            }

            start = time.time()

            response = session.get(
                url,
                headers=headers,
                timeout=TIMEOUT
            )

            ping = round((time.time() - start) * 1000)

            if response.status_code == 200:
                log(f"ONLINE ✅ {ping}ms")

            else:
                log(f"STATUS {response.status_code} ⚠️")

        except Exception as e:
            log(f"ERROR ❌ {e}")

        time.sleep(PING_INTERVAL)

# ==========================================
# MULTI THREADS
# ==========================================

print("🚀 ADVANCED CODESANDBOX MONITOR STARTED")

for i in range(3):
    t = threading.Thread(target=keep_alive)
    t.daemon = True
    t.start()

while True:
    time.sleep(999999)
