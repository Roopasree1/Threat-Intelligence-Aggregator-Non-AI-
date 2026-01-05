import requests
from utils.regex_patterns import IP_REGEX, DOMAIN_REGEX

def parse_rss_feed(url, source_name):
    response = requests.get(url)
    data = response.text
    iocs = []

    for ip in IP_REGEX.findall(data):
        iocs.append({"type": "ip", "value": ip, "source": source_name})

    for domain in DOMAIN_REGEX.findall(data):
        iocs.append({"type": "domain", "value": domain, "source": source_name})

    return iocs
