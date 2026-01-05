
import json
from collections import defaultdict

def correlate_iocs(normalized_iocs):
    correlation_map = defaultdict(lambda: {
        "type": "",
        "value": "",
        "sources": set(),
        "count": 0,
        "risk_level": ""
    })

    for ioc in normalized_iocs:
        key = (ioc["type"], ioc["value"])

        correlation_map[key]["type"] = ioc["type"]
        correlation_map[key]["value"] = ioc["value"]
        correlation_map[key]["sources"].add(ioc["source"])
        correlation_map[key]["count"] += 1

    correlated_results = []

    for entry in correlation_map.values():
        count = entry["count"]

        if count >= 5:
            entry["risk_level"] = "HIGH"
        elif count >= 3:
            entry["risk_level"] = "MEDIUM"
        else:
            entry["risk_level"] = "LOW"

        entry["sources"] = list(entry["sources"])
        correlated_results.append(entry)

    with open("output/correlated_iocs.json", "w") as f:
        json.dump(correlated_results, f, indent=2)

    print(f"[+] Correlated {len(correlated_results)} unique indicators")
    return correlated_results
