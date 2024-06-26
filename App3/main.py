from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
# p for portrait or l for landscape
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(255, 204, 229)  # r g b parameters
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1)

    r = range(26)
    for i in r:
        pdf.line(x1=10, y1=22+10*i, x2=200, y2=22+10*i)

    # set the footer
    pdf.ln(260)  # break line with 260mm
    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(w=0, h=10, txt=row['Topic'], align="R")

    for item in range(row['Pages']-1):
        pdf.add_page()
        # adicionamos paginas em branco

        pdf.ln(272)  # 260 + 12 (height of the text)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(150, 150, 150)
        pdf.cell(w=0, h=10, txt=row['Topic'], align="R")
        r = range(26)
        for i in r:
            pdf.line(x1=10, y1=22 + 10 * i, x2=200, y2=22 + 10 * i)

pdf.output("output.pdf")
