# -*- coding: utf-8 -*-
#!/usr/bin/env python
__author__ = 'kalcho'
# get teams from Serbian Basketball League

import requests
from bs4 import BeautifulSoup
import pandas
import urlparse


url = 'http://www.kls.rs/timovi.php'
response = requests.get(url)
if response.status_code == 200:
    bsObj = BeautifulSoup(response.text, "html.parser")
    tables = bsObj.find_all("table", class_="naslov_tabele", width=190)
    teams = []
    team_cities = []
    team_urls = []
    for table in tables:
        tr = table.find_all("tr")
        for r in tr:
            if r.td.a is not None:
                info = r.td.a
                teams.append(info.text)
                team_url = info['href']
                team_urls.append(urlparse.urljoin(url.rsplit('/', 1)[-2], team_url))
            else:
                city = r.td
                team_cities.append(city.text)

d = {"team_city": team_cities, "url": team_urls}
teams = pandas.DataFrame(d, index=teams)
teams.index.name = "team"
print teams