from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
import reportlab.lib.units as unit
import reportlab.lib.pagesizes as pagesizes


pdfmetrics.registerFont(UnicodeCIDFont("HeiseiKakuGo-W5"))


pdf = canvas.Canvas("example.pdf", pagesize=pagesizes.A4)


title = "我是台灣人！"
for char in title:
    pdf.setFont("HeiseiKakuGo-W5", 210 * unit.mm)
    h = (297 - 210) / 2 * unit.mm

    pdf.drawString(0 * unit.mm, h, char)
    pdf.showPage()

    
pdf.save()
