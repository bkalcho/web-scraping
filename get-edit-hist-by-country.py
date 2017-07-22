#!/usr/bin/env python
__author__ = 'kalcho'


import urllib2
from bs4 import BeautifulSoup
import datetime
import random
import re
import json


random.seed(datetime.datetime.now())
def get_links(article_url):
    """Find all internal links on the article page"""
    html = urllib2.urlopen("http://en.wikipedia.org/" + article_url)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id":"bodyContent"})\
        .find_all("a", href=re.compile("^(/wiki/)((?!:).)*$"))


def get_history_ips(page_url):
    #Format of revision history pages is:
    #http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    page_url = page_url.replace("/wiki/", "")
    history_url = "http://en.wikipedia.org/w/index.php?title=" + page_url +\
        "&action=history"
    print "history url is: " + history_url
    html = urllib2.urlopen(history_url)
    bsObj = BeautifulSoup(html, "html.parser")
    #finds only the links with class "mw-anonuserlink" which has IP addresses
    #instead of usernames
    ip_addresses = bsObj.find_all("a", {"class":"mw-anonuserlink"})
    address_list = set()
    for ip_addr in ip_addresses:
        address_list.add(ip_addr.get_text())
    return address_list

def get_country(ip_addr):
    try:
        response = urllib2.urlopen("http://freegeoip.net/json/" + ip_addr)\
            .read().decode("utf-8")
    except HTTPError:
        return None
    response_json = json.loads(response)
    return response_json.get("country_code")


links = get_links("/wiki/Python_(programming_language)")

while (len(links) > 0):
    for link in links:
        print "------------------"
        history_ips = get_history_ips(link.attrs["href"])
        for history_ip in history_ips:
            country = get_country(history_ip)
            if country is not None:
                print history_ip + " is from " + country
    
    new_link = links[random.randint(0, len(links) - 1)].attrs["href"]
    links = get_links(new_link)
