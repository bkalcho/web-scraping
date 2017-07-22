#!/usr/bin/env python
__author__ = 'kalcho'

import requests
from lxml import html


link = "http://sdirwmp.org/contact-us"
response = requests.get(link, allow_redirects=False)
source_code = response.content
html_elem = html.fromstring(source_code)

# write data to CSV file
csv_filename = "names_and_phones.csv" # name of the file you want to save your data
csv_fd = open(csv_filename, "w") # create a csv file
col_names = "Name, Phone\n" # column titles
csv_fd.write(col_names)

td_elems = html_elem.cssselect("[valign=top]")
for elem in td_elems:
    text = elem.text_content()
    split_text = text.split('\r\n')
    name = split_text[2].strip()
    phone = split_text[-3].strip()
    csv_fd.write(name + ',' + phone + ',\n')