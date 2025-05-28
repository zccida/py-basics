
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
from PIL import Image


pdf = FPDF()

name_input = input("Name: ")
pdf.add_page()
pdf.set_font("Arial", size=16)

pdf.cell(0, 10, "CS50 Shirtificate", align='C')
image_width = 150
image_height = 50

img_x = (210 - image_width) / 2
pdf.image("shirtificate.png", x=img_x, y=image_height, w=image_width)
pdf.set_text_color(255, 255, 255)
name_loc = image_height + 50
pdf.set_xy(0, name_loc)
pdf.cell(0, 10, f"{name_input} took CS50", align='C')

pdf.output("shirtificate.pdf")
