from osint.fetch_live_feeds import fetch_feeds
from normalizer.normalize import normalize_iocs
from correlation.correlate import correlate_iocs
from blocklists.generate_blocklists import generate_blocklists
from reports.report_generator import generate_report
from reports.export_csv import export_csv


import os

def main():
    print("\n=== Threat Intelligence Aggregator Started ===\n")

    # 1️⃣ Fetch live OSINT feeds
    print("[1] Fetching live OSINT feeds...")
    fetch_feeds()

    # 2️⃣ Normalize all feeds
    print("[2] Normalizing IOC feeds...")
    normalized_iocs = normalize_iocs()

    # 3️⃣ Correlate indicators
    print("[3] Correlating indicators...")
    correlated_iocs = correlate_iocs(normalized_iocs)

    # 4️⃣ Generate blocklists
    print("[4] Generating blocklists...")
    generate_blocklists()

    # 5️⃣ Generate report
    print("[5] Generating threat intelligence report...")
    generate_report()

    print("[6] Exporting CSV report...")
    export_csv()


    print("\n=== Threat Intelligence Aggregator Completed ===")
    print("Check the 'output/' directory for results\n")

if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)
    main()
