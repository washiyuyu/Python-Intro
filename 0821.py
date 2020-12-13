#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 23:01:41 2020

@author: linkuanyu
"""

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
import reportlab.lib.units as unit
import reportlab.lib.pagesizes as pagesizes


pdfmetrics.registerFont(UnicodeCIDFont("HeiseiKaKuGo-W5"))


pdf = canvas.Canvas("example.pdf", pagesize=pagesizes.A4)
pdf.setFont("HeiseiKaKuGo-W5", 14)
pdf.drawString(10 * unit.mm, 270 * unit.mm, "My first PDF")
pdf.save()