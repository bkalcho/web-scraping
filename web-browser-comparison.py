#!/usr/bin/env python
__author__ = 'kalcho'

import urllib2
import csv
from bs4 import BeautifulSoup


html = urllib2.urlopen("https://en.wikipedia.org/wiki/Comparison_of_web_browsers")
bsObj = BeautifulSoup(html, "html.parser")
table = bsObj.find_all("table", {"class": "wikitable"})[0]
rows = table.find_all("tr")
csv_fd = open("browsers.csv", "wt")
writer = csv.writer(csv_fd)
try:
    for row in rows:
        csv_row = []
        for cell in row.find_all(["td", "th"]):
            csv_row.append(cell.get_text())
            writer.writerow(csv_row)
finally:
    csv_fd.close()