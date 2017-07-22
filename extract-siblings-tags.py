#!/usr/bin/env python
__author__ = 'kalcho'

import urllib2
from bs4 import BeautifulSoup


html = urllib2.urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

# get next siblings of the table header row
for sibling in bsObj.find("table", {"id":"giftList"}).tr.next_siblings:
    print sibling

# beside next_siblings() method we can also use previous_siblins(). Also
# next_sibling() and previous_sibling() method exist. These methods
# return just first sibling in line, instead of all siblings that follow
# or precede