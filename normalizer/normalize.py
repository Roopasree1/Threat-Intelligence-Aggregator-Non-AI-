
import os
import json
from datetime import datetime

def normalize_iocs():
    normalized = []
    feeds_root = "feeds"

    for root, _, files in os.walk(feeds_root):
        for file in files:
            if not file.endswith((".txt", ".csv", ".json")):
                continue

            source_name = file
            file_path = os.path.join(root, file)

            try:
                with open(file_path, "r", errors="ignore") as f:
                    for line in f:
                        value = line.strip()
                        if not value:
                            continue

                        normalized.append({
                            "type": detect_type(value),
                            "value": value,
                            "source": source_name,
                            "timestamp": datetime.utcnow().isoformat()
                        })
            except Exception as e:
                print(f"[!] Failed normalizing {file}: {e}")

    os.makedirs("output", exist_ok=True)
    with open("output/normalized_iocs.json", "w") as out:
        json.dump(normalized, out, indent=2)

    print(f"[+] Normalized {len(normalized)} indicators")
    return normalized


def detect_type(value):
    if value.count(".") == 3:
        return "ip"
    if value.startswith("http"):
        return "url"
    if "@" in value:
        return "email"
    if len(value) in [32, 40, 64]:
        return "hash"
    return "domain"
