#!/usr/bin/env python
__author__ = 'kalcho'
# scrape image file from the website

from urllib import urlopen, urlretrieve
from bs4 import BeautifulSoup


html = urlopen('http://www.pythonscraping.com')
bsObj = BeautifulSoup(html, "html.parser")
image_location = bsObj.find("a", {"id": "logo"}).find("img")["src"]
urlretrieve(image_location, image_location.split('/')[-1])
