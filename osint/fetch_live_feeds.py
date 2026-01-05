import requests
import os
from datetime import datetime

FEEDS = {
    "ips": "https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/firehol_level1.netset",
    "urls": "https://urlhaus.abuse.ch/downloads/text/",
    "phishing": "https://openphish.com/feed.txt"
}

OUTPUT_DIR = "feeds/txt_feeds"

def fetch_feeds():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for name, url in FEEDS.items():
        try:
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                filename = f"{OUTPUT_DIR}/{name}_feed_{datetime.utcnow().date()}.txt"
                with open(filename, "w") as f:
                    f.write(response.text)

                print(f"[+] Fetched {name} feed → {filename}")
            else:
                print(f"[-] Failed to fetch {name}")

        except Exception as e:
            print(f"[!] Error fetching {name}: {e}")

if __name__ == "__main__":
    fetch_feeds()
