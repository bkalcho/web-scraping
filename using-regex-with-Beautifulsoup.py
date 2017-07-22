#!/usr/bin/env python
__author__ = 'kalcho'

import urllib2
from bs4 import BeautifulSoup


html = urllib2.urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")
# extract image paths that start with ../img/gifts/img and and in jpg
images = bsObj.find_all("img", {"src":urllib2.re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print image["src"]

# to retrive all attributes of some tag we can use attrs eg. myTag.attrs.
# This returns a dictionary, so particular attribute can be accessed on
# the next way myTag.attrs["src"]

# using lambda expressions in findAll function: Argument of the lambda
# function must be tag object, and lambda function must return boolean
# value, eg. bsObj.findAll(lambda tag: len(tag.attrs) == 2)