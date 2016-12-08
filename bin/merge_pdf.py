#!/usr/bin/env python3

import os
import glob
from PyPDF2 import PdfFileReader, PdfFileMerger

pdf_files = glob.glob('*.pdf')
merger = PdfFileMerger()
pdf_files = sorted(pdf_files)

for filename in pdf_files:
    merger.append(PdfFileReader(os.path.join(os.getcwd(), filename), "rb"))

merger.write(os.path.join("/home/wadeallen/Desktop", "merged_pdfs.pdf"))

