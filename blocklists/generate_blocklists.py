import json
import os

def generate_blocklists(input_file="output/correlated_iocs.json",
                        output_dir="output"):

    with open(input_file, "r") as f:
        iocs = json.load(f)

    firewall_ips = set()
    domains = set()
    hashes = set()

    for ioc in iocs:
        # include MEDIUM + HIGH for demo realism
        if ioc["risk_level"] in ["HIGH", "MEDIUM"]:
            if ioc["type"] == "ip":
                firewall_ips.add(ioc["value"])
            elif ioc["type"] in ["domain", "url"]:
                domains.add(ioc["value"])
            elif ioc["type"] == "hash":
                hashes.add(ioc["value"])

    os.makedirs(output_dir, exist_ok=True)

    with open(f"{output_dir}/firewall_blocklist.txt", "w") as f:
        f.write("\n".join(firewall_ips))

    with open(f"{output_dir}/domain_blocklist.txt", "w") as f:
        f.write("\n".join(domains))

    with open(f"{output_dir}/hash_blocklist.txt", "w") as f:
        f.write("\n".join(hashes))

    print("[+] Blocklists generated (IP / Domain / Hash)")
