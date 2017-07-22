#!/usr/bin/env python
__author__ = 'kalcho'

import requests
from bs4 import BeautifulSoup
import pandas

url = 'http://www.espn.com/nba/teams'
response = requests.get(url)
bsObj = BeautifulSoup(response.content, "html.parser")
tables = bsObj.find_all("ul", class_="medium-logos")

teams = []
prefix_1 = []
prefix_2 = []
teams_urls = []
for table in tables:
    lis = table.find_all("li")
    for l in lis:
        info = l.div.h5.a
        teams.append(info.text)
        url = info["href"]
        teams_urls.append(url)
        prefix_1.append(url.split('/')[-2])
        prefix_2.append(url.split('/')[-1])

dic = {"url": teams_urls, "prefix_2": prefix_2, "prefix_1": prefix_1}
teams = pandas.DataFrame(dic, index=teams)
teams.index.name = "team"
print teams