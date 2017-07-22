#!/usr/bin/env python
__author__ = 'kalcho'
# Find all article links in one Wikipedia article

import urllib2
from bs4 import BeautifulSoup
import datetime
import random
import re


random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urllib2.urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",
                        href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print newArticle
    links = getLinks(newArticle)
