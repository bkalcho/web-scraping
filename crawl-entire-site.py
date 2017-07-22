#!/usr/bin/env python
__author__ = 'kalcho'
# Crawling all article links found on wiki pages

import urllib2
from bs4 import BeautifulSoup
import re

pages = set()
def get_links(pageUrl):
    global pages
    html = urllib2.urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.find_all("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print newPage
                pages.add(newPage)
                get_links(newPage)


get_links("")
