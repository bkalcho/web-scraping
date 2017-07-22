#!/usr/bin/env
__author__ = 'kalcho'
# Find all links on some web page

import requests
from HTMLParser import HTMLParser
import re
import urlparse


class LinkParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
    
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for name, value in attrs:
                if name == 'href':
                    if re.match(r'^//.*', value):
                        print value[2:]
                    elif re.match(r'^/.+', value):
                        print urlparse.urljoin(url, value)
                    elif re.match(r'^/$', value):
                        pass
                    else:
                        print value


url = "http://www.youtube.com"
response = requests.get(url)
parser = LinkParser()
parser.feed(response.text)
