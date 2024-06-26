import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# Automation program, without a graphical user interface. For internal use.
# Pandas need openpyxl package to read Excel files. Install it!

# Make a list of files
filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:

    pdf = FPDF(orientation="P", unit="mm")
    pdf.add_page()

    file_name = Path(filepath).stem
    invoice_nr = file_name.split("-")[0]
    date = file_name.split("-")[1]

    pdf.set_font(family='Times', size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1)

    pdf.set_font(family='Times', size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    columns = list(df.columns)
    titles = [item.replace("_", " ").title() for item in columns]

    # Add header
    pdf.set_font(family='Times', size=10, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=str(titles[0]), border=1)
    pdf.cell(w=70, h=8, txt=str(titles[1]), border=1)
    pdf.cell(w=35, h=8, txt=str(titles[2]), border=1)
    pdf.cell(w=30, h=8, txt=str(titles[3]), border=1)
    pdf.cell(w=25, h=8, txt=str(titles[4]), border=1, ln=1)

    # Add rows
    for index, row in df.iterrows():
        pdf.set_font(family='Times', size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row['product_id']), border=1)
        pdf.cell(w=70, h=8, txt=str(row['product_name']), border=1)
        pdf.cell(w=35, h=8, txt=str(row['amount_purchased']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['price_per_unit']), border=1)
        pdf.cell(w=25, h=8, txt=str(row['total_price']), border=1, ln=1)

    # Add total price
    total_sum = str(df["total_price"].sum())
    pdf.set_font(family='Times', size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=70, h=8, txt="", border=1)
    pdf.cell(w=35, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=25, h=8, txt=total_sum, border=1, ln=1)

    # Add text in the bottom
    pdf.set_font(family='Times', size=10, style="B")
    pdf.cell(w=25, h=8, txt=f"The total price is {total_sum}", ln=1)

    pdf.set_font(family='Times', size=14, style="B")
    pdf.cell(w=25, h=8, txt=f"PythonHow")
    pdf.image("pythonhow.png", w=10)

    pdf.output(f"PDFs/{file_name}.pdf")
