#!/usr/bin/env python
__author__ = 'kalcho'

import requests
from lxml import html
import urllib2

base_url = "http://www.sandag.org" # page we want to scrape
response = requests.get(base_url, allow_redirects=False) # get HTTP GET response, and do not allow redirects
source_code = response.content # source code of the page
html_elem = html.fromstring(source_code) # get htmlElement
html_elem.make_links_absolute(base_url, resolve_base_href=True)
elements = html_elem.iterlinks()
num_pdf = 0
for el in elements:
    link = el[2]
    file_ext = link.split('.')[-1]
    if file_ext == 'pdf':
        download_dir = "downloaded_pdfs\pdf%s.pdf" % num_pdf
        fd = open(download_dir, "wb")
        res = urllib2.urlopen(link)
        pdf = res.read()
        fd.write(pdf)
        fd.close()
        num_pdf += 1