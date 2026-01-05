import csv
from utils.validators import (
    is_valid_ip, is_valid_domain,
    is_valid_url, is_valid_email, is_valid_hash
)

def parse_csv_feed(file_path, source_name):
    iocs = []

    with open(file_path, newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for cell in row:
                if is_valid_ip(cell):
                    iocs.append({"type": "ip", "value": cell, "source": source_name})
                elif is_valid_domain(cell):
                    iocs.append({"type": "domain", "value": cell, "source": source_name})
                elif is_valid_url(cell):
                    iocs.append({"type": "url", "value": cell, "source": source_name})
                elif is_valid_email(cell):
                    iocs.append({"type": "email", "value": cell, "source": source_name})
                elif is_valid_hash(cell):
                    iocs.append({"type": "hash", "value": cell, "source": source_name})

    return iocs
