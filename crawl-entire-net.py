#!/usr/bin/env python
__author__ = 'kalcho'
# Crawl entire internet by hopping from one site to another site by
# following random external link from start page. If external link not
# found, follow random internal link, and on that page get external
# random external link.


import urllib2
from bs4 import BeautifulSoup
import re
import datetime
import random


pages = set()
random.seed(datetime.datetime.now())


# retrives a list of all Internal links found on a page
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    # Finds all links that begin with a "/"
    for link in bsObj.find_all("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks


# retrieves a list of all external links found on a page
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # finds all links that start with a "http" or "www" that do not
    # contain the current URL
    for link in bsObj.find_all("a",
                        href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts


def getRandomExternalLink(startingPage):
    html = urllib2.urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(bsObj, startingPage)
        return getRandomExternalLink(internalLinks[random.randint(0,
                                    len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingPage)
    print "Random external link is: " + externalLink
    followExternalOnly(externalLink)


followExternalOnly("http://oreilly.com")