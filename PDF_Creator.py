# refrernce : https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html
# Created by Sowmya.R
import os
from fpdf import FPDF

#creating a pdf 
# A4 portrait and the measure unit is millimeter ==> this is default even if the parameter is not given
#other measuring units ==> pt, cm, in
#a4 page 210 X 297 mm
pdf = FPDF('P', 'mm', 'A4')
pdf.add_page() 
# bold = B, italics=I, underline = U. Font size in Points
# standard font names are Arial, Times, Courier, Symbol and ZapfDingbats
# Arial bold 16
pdf.set_font('Arial', 'B', 16) 

## We can now print a cell with cell. A cell is a rectangular area, possibly framed, which contains some text. 
# It is output at the current position. 
# We specify its dimensions, its text (centered or aligned), if borders should be drawn, and 
# where the current position moves after it (to the right, below or to the beginning of the next line).
#cell(width, height, borderYes?,gotoNewlineNext?,textalignment)
pdf.cell(190, 10, 'Main Title', 1, 1, 'C')
# pdf.ln(10) # new line after 10 pts
pdf.set_font('Arial', 'B', 14) 
pdf.cell(100,10,'Section 1',1,1,'A')
pdf.set_font('Arial','',12)
pdf.cell(50,10,'Attribute1',0,0)
pdf.cell(50,10,'value1',0,1)
pdf.cell(50,10,'Attribute2',0,0)
pdf.cell(50,10,'value2',0,1)
pdf.cell(50,10,'Attribute3',0,0)
pdf.cell(50,10,'value3',0,0)
pdf.cell(50,10,'Attribute4',0,0)
pdf.cell(50,10,'value4',0,1)

#now implement text colors
pdf.ln(10)
pdf.set_font('Arial', 'B', 14) 
pdf.cell(100,10,'Section 2',1,1,'A')
pdf.set_font('Arial','',12)
pdf.set_text_color (0,0,255)
pdf.cell(50,10,'Attribute21',0,0)
pdf.set_text_color (0,0,0)
pdf.cell(50,10,'value21',0,0)
pdf.set_text_color (0,0,255)
pdf.cell(50,10,'Attribute21',0,0)
pdf.set_text_color (0,0,0)
pdf.cell(50,10,'value21',0,1)

pdf.ln(10)
pdf.set_font('Arial', 'B', 14) 
pdf.cell(100,10,'Section 3',1,1,'A')
pdf.set_font('Arial', 'B', 12) 
pdf.cell(100,10,'Section 3: subtitle',1,1,'A')
pdf.set_font('Arial', '', 14) 

pdf.cell(60,10,'image 1',1,0,'A')
pdf.cell(60,10,'image 2',1,0,'A')
pdf.cell(60,10,'image 3',1,1,'A')

pdf.image("butterfly.JPG", 10, 130,40,40,'JPG')
pdf.image("butterfly.JPG", 70, 130,40,40,'JPG')
pdf.image("butterfly.JPG", 130, 130,40,40,'JPG')

pdf.output('pdfcreator.pdf', 'F')
