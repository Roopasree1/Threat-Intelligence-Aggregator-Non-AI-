from utils.regex_patterns import (
    IP_REGEX, DOMAIN_REGEX, URL_REGEX,
    EMAIL_REGEX, MD5_REGEX, SHA1_REGEX, SHA256_REGEX
)
from utils.validators import (
    is_valid_ip, is_valid_domain,
    is_valid_url, is_valid_email, is_valid_hash
)

def parse_txt_feed(file_path, source_name):
    iocs = []

    with open(file_path, "r", errors="ignore") as file:
        data = file.read()

    for ip in IP_REGEX.findall(data):
        if is_valid_ip(ip):
            iocs.append({"type": "ip", "value": ip, "source": source_name})

    for domain in DOMAIN_REGEX.findall(data):
        if is_valid_domain(domain):
            iocs.append({"type": "domain", "value": domain, "source": source_name})

    for url in URL_REGEX.findall(data):
        if is_valid_url(url):
            iocs.append({"type": "url", "value": url, "source": source_name})

    for email in EMAIL_REGEX.findall(data):
        if is_valid_email(email):
            iocs.append({"type": "email", "value": email, "source": source_name})

    for hash_value in MD5_REGEX.findall(data) + SHA1_REGEX.findall(data) + SHA256_REGEX.findall(data):
        if is_valid_hash(hash_value):
            iocs.append({"type": "hash", "value": hash_value, "source": source_name})

    return iocs
