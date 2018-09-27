#!/usr/bin/env python3

import os
import glob
from PyPDF2 import PdfFileReader, PdfFileMerger

files = glob.glob('*.markdown')
files = sorted(files)

for name in files:
	base = name.split('.')[0]
	os.system('pandoc "{}" -o "{}.pdf" --template=lester.tex'.format(name,base))
	print ('Converted {} ----> pdf'.format(base))

pdf_files = sorted(glob.glob('*.pdf'))
merger = PdfFileMerger()

for filename in pdf_files:
    merger.append(PdfFileReader(os.path.join(os.getcwd(), filename), "rb"))

merger.write(os.path.join("/home/wadeallen/Desktop", "merged_full.pdf"))


