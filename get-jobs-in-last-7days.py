#!/usr/bin/env python
__author__ = 'kalcho'

import requests
from lxml import html
import urlparse


url = 'https://poslovi.infostud.com/oglasi-za-posao#dist=&last_search_time=&submit=0&q=&city[]=35&vreme_postavljanja=7&rok_konkursa=&firma_uid=&education=&vrste_kategorija_posla=&jezik=&sort='
response = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'})
tree = html.fromstring(response.content)

job_positions = tree.xpath('//body/div/div/div/form/div/div/div/div/div/div/ul/li/h2/@title')
job_positions = [job_positions[i].strip() for i in xrange(0, len(job_positions))]
job_links = tree.xpath('//body/div/div/div/form/div/div/div/div/div/div/ul/li/h2/a[contains(@href, "/posao/")]')
job_links = [urlparse.urljoin('https://poslovi.infostud.com/', u) for u in job_links]

print job_positions
print job_links


# items = tree.xpath('//body/div/div/div/form/div/div/div/div/ul/li/a/@href | //body/div/div/div/form/div/div/div/div/ul/li/a/text()')
# print items
# pages = []
# for href, page_num in zip(*[iter(items)]*2):
#     if str(page_num).isdigit():
#         pages.append((int(page_num), href))

# print pages