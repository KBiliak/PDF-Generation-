import pandas as pd
from fpdf import FPDF

pdf = FPDF(orientation="P", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)


df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    #header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(0,100, 200)
    pdf.cell(w=0, h=0, txt=row["Topic"], align="L")
    for y in range(20,280,10):
        pdf.line(10, y, 200, y)



    #footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=12)
    pdf.set_text_color(0, 100, 200)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"]):
        pdf.add_page()

        pdf.ln(265)
        pdf.set_font(family="Times", style="I", size=12)
        pdf.set_text_color(0, 100, 200)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
        for y in range(20, 280, 10):
            pdf.line(10, y, 200, y)



pdf.output("topics.pdf")

