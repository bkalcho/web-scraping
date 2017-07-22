#!/usr/bin/env python
__author__ = 'kalcho'

import requests
from lxml import html


url = 'http://poslovi.infostud.com'
response = requests.get(url)
parsed_body = html.fromstring(response.text)
jobs = parsed_body.xpath('//body/div/div/div/div/div/div/ul/li/h3/a/text()')
print jobs
print parsed_body.xpath('//a/@href')