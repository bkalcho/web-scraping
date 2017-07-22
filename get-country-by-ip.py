#!/usr/bin/env python
__author__ = 'kalcho'

import json
import urllib2
from bs4 import BeautifulSoup


def get_country(ip_addr):
    """Get Country name to which IP address has been assigned"""
    html = urllib2.urlopen('http://freegeoip.net/json/' + ip_addr).read()\
            .decode('utf-8')
    responseJson = json.loads(html)
    return responseJson.get('country_code')


while True:
    ip = raw_input("Input desired IP address ('q'-quit)? ")
    if ip != 'q':
        print get_country(ip)
    else:
        break