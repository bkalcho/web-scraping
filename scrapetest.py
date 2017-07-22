#!/usr/bin/env python
__author__ = 'kalcho'


import urllib2
from bs4 import BeautifulSoup

link = "http://pythonscraping.com/pages/page1.html"
def getTitle(url):
    try:
        html = urllib2.urlopen(url)
    except urllib2.HTTPError, e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except AttributeError, e:
        return None
    return title


title = getTitle(link)
if title == None:
    print "Title could not be found"
else:
    print title