
'''
The orientation of the PDF should be Portrait.
The format of the PDF should be A4, which is 210mm wide by 297mm tall.
The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
The shirt’s image should be centered horizontally.
The user’s name should be on top of the shirt, in white text.
'''

import re
import sys
from fpdf import FPDF


pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, txt="CS50 Shirtificate", ln=True, align='C')
pdf.image("shirtificate.png")
pdf.output("testo.pdf")
