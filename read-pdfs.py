#!/usr/bin/env python
__author__ = 'kalcho'

import requests
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO, BytesIO, open


def readpdf(pdf_file):
    fd = StringIO(pdf_file.content)
    print fd.encoding
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pagenums = set()
    for page in PDFPage.get_pages(fd, pagenums):
        interpreter.process_page(page)
    device.close()

    content = retstr.getvalue()
    retstr.close
    fd.close()
    return content


pdf_file = requests.get("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
# if file downloaded locally, uncomment next line, and comment previous line
#pdf_file = open("pages/warandpeace/chapter1.pdf")
output_string = readpdf(pdf_file)
print output_string
pdf_file.close()