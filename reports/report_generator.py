import json
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_report(input_file="output/correlated_iocs.json"):
    with open(input_file, "r") as f:
        iocs = json.load(f)

    pdf_path = "output/final_report.pdf"
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4

    y = height - 50
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Threat Intelligence Report")
    y -= 30

    c.setFont("Helvetica", 10)
    c.drawString(50, y, f"Generated on: {datetime.utcnow()} UTC")
    y -= 30

    for ioc in iocs[:40]:  # first 40 high-value IOCs
        line = f"{ioc['type']} | {ioc['value']} | {ioc['risk_level']} | {ioc['count']} sources"
        c.drawString(50, y, line)
        y -= 15
        if y < 50:
            c.showPage()
            y = height - 50

    c.save()
    print("[+] PDF report generated → output/final_report.pdf")
