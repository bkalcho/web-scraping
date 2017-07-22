#!/usr/bin/env python
__author__ = 'kalcho'

import requests
from lxml import html


base_url = 'http://www.pulitzer.org/prize-winners-by-year/2017'
response = requests.get(base_url, allow_redirects=False)
source_code = response.content.decode('latin-1')
elem_tree = html.fromstring(source_code)
start_year = elem_tree.xpath("//div/text()")
print start_year