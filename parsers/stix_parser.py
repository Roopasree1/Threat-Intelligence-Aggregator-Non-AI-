import json

def parse_stix_feed(file_path, source_name):
    iocs = []

    with open(file_path, "r", encoding="utf-8") as file:
        stix_data = json.load(file)

    for obj in stix_data.get("objects", []):
        if obj.get("type") == "indicator":
            pattern = obj.get("pattern", "")
            if "ipv4-addr:value" in pattern:
                value = pattern.split("'")[1]
                iocs.append({"type": "ip", "value": value, "source": source_name})
            elif "domain-name:value" in pattern:
                value = pattern.split("'")[1]
                iocs.append({"type": "domain", "value": value, "source": source_name})
            elif "file:hashes" in pattern:
                value = pattern.split("'")[1]
                iocs.append({"type": "hash", "value": value, "source": source_name})

    return iocs
