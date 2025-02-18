import requests
import time
from datetime import datetime

# List of deployed app URLs
URLS = [
    "https://facial-expression-classification.onrender.com/",
]



def ping_apps():
    for url in URLS:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                print(f"[{datetime.now()}] Ping successful: {url}")
            else:
                print(f"[{datetime.now()}] Ping failed: {url} with status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"[{datetime.now()}] Error pinging {url}: {e}")



if __name__ == "__main__":

    # Run pings 4 times (every 14 minutes) within an hour
    for _ in range(4):
        ping_apps()
        time.sleep(840)  # Wait for 14 minutes (840 seconds)
