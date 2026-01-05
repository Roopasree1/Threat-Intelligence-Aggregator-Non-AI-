import csv
import json

def export_csv(input_file="output/correlated_iocs.json",
               output_file="output/ioc_report.csv"):

    with open(input_file, "r") as f:
        data = json.load(f)

    with open(output_file, "w", newline="") as csvfile:
        fieldnames = ["type", "value", "risk_level", "count", "sources"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for ioc in data:
            writer.writerow({
                "type": ioc["type"],
                "value": ioc["value"],
                "risk_level": ioc["risk_level"],
                "count": ioc["count"],
                "sources": ", ".join(ioc["sources"])
            })

    print("[+] CSV report generated")
