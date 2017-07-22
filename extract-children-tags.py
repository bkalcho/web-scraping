#/usr/bin/env python
__author__ = 'kalcho'

import urllib2
from bs4 import BeautifulSoup


html = urllib2.urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

# get children of the table tag
for child in bsObj.find("table", {"id":"giftList"}).children:
    print child

# Beside children, we can also use method descendants, which returns all
# descendands. All children are descendands but not all descendants are
# children, just first line descendants are children.