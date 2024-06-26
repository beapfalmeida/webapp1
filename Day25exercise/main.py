from fpdf import FPDF
import glob
from pathlib import Path

files = glob.glob("Text_files/*txt")
pdf = FPDF(orientation="P", unit="mm")


for file in files:
    filename = Path(file).stem
    name = filename.capitalize()
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=50, h=10, txt=name, ln=1)

    pdf.set_font(family="Times", size=12)
    with open(file) as doc:
        text = doc.read()
    pdf.multi_cell(w=0, h=6, txt=text)

pdf.output("output.pdf")

