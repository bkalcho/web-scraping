#!/usr/bin/env python
__author__ = 'kalcho'
# Extract job vacancies from GET site from careers page

import urllib2
from bs4 import BeautifulSoup


link = "http://www.global-engineering-technologies.com/careers-get/"
html = urllib2.urlopen(link)
bsObj = BeautifulSoup(html, "html.parser")
workPositions = bsObj.find_all("a", {"rel":"nofollow"})
i = 1
for workposition in workPositions:
    print "%d.\tWork position: %s" % (i, workposition.get_text())
    print "\tLink to position description: " + workposition.attrs["href"] + "\n"
    i += 1