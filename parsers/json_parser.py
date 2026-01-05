import json
from utils.validators import (
    is_valid_ip, is_valid_domain,
    is_valid_url, is_valid_email, is_valid_hash
)

def parse_json_feed(file_path, source_name):
    iocs = []

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    def extract(value):
        if isinstance(value, str):
            if is_valid_ip(value):
                iocs.append({"type": "ip", "value": value, "source": source_name})
            elif is_valid_domain(value):
                iocs.append({"type": "domain", "value": value, "source": source_name})
            elif is_valid_url(value):
                iocs.append({"type": "url", "value": value, "source": source_name})
            elif is_valid_email(value):
                iocs.append({"type": "email", "value": value, "source": source_name})
            elif is_valid_hash(value):
                iocs.append({"type": "hash", "value": value, "source": source_name})
        elif isinstance(value, dict):
            for v in value.values():
                extract(v)
        elif isinstance(value, list):
            for v in value:
                extract(v)

    extract(data)
    return iocs
