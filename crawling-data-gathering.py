#/usr/bin/env python
__author__ = 'kalcho'
#get some data from crowled site

import urllib2
from bs4 import BeautifulSoup
import re


pages = set()
def getLinks(pageUrl):
    global pages
    html = urllib2.urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    try:
        print bsObj.h1.get_text()
        print bsObj.find(id="mw-content-text").find_all("p")[0]
        print bsObj.find(id="ca-edit").find("span").find("a").attrs['href']
    except AttributeError:
        print "This page is missing something! No worries though!"
    
    for link in bsObj.find_all("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # we have encountered a new page
                newPage = link.attrs['href']
                print "--------------------\n"+newPage
                pages.add(newPage)
                getLinks(newPage)


getLinks("")