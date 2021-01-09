# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:18:48 2021

@author: Jishnu

Merge pdf

merge pdf to the file given 

glob will search for all pdf in the dir, if we want to specify some name, give it as a list []
"""
from pikepdf import Pdf
from glob import glob
import os

filepath= "G:\Developments\Merge pdf"
os.chdir(filepath)
pdf = Pdf.open('B224-CDU-TPL-000-TS-GN-PR0042-0003_SIL Study Procedure_Rev.1.pdf')


pdf = Pdf.new()
for file in glob('*.pdf'):
    src = Pdf.open(file)
    pdf.pages.extend(src.pages)
    
pdf.save('merged.pdf')