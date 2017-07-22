#!/usr/bin/env python
__author__ = 'kalcho'

import csv
from urllib2 import urlopen
from bs4 import BeautifulSoup


html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html, "html.parser")
# The main comparison table is currently the first table on the page
table = bsObj.find_all("table", {"class": "wikitable"})[0]
rows = table.find_all("tr")

csv_file = open("editors.csv", "wt")
writer = csv.writer(csv_file)
try:
    for row in rows:
        csv_row = []
        for cell in row.find_all(["td", "th"]):
            csv_row.append(cell.get_text())
            writer.writerow(csv_row)

finally:
    csv_file.close()