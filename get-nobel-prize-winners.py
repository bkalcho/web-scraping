#!/usr/bin/env python
__author__ = 'kalcho'
# get nobel prize winners for each year

import requests
from lxml import html
import pandas


base_url = 'http://www.nobelprize.org/nobel_prizes/lists/all/index.html'
response = requests.get(base_url, allow_redirects=False)
source_code = response.content.decode('latin-1')
element_tree = html.fromstring(source_code)
l = element_tree.xpath('//div[@class="by_year"]')
year_elements = element_tree.xpath('//div[@class="row"]/div/h3')
years = []
categories = []
winners = []
synopsises = []
csv_file = "nobel_prize_winners.csv"
fd = open(csv_file, "w")
# write csv column header
fd.write("Year,Category,Winners,Synopsis\n")

for y_el in year_elements:
    year = y_el.text_content().strip()
    el = y_el.getnext()
    
    while el.tag == 'div':
        category = el.find(path="h3/a").text_content().strip()
        winner = ", ".join([e.text_content().strip() for e in el.findall(path="h6/a")])
        synopsis = el.find(path="p").text_content().strip()
        
        years.append(year)
        categories.append(category)
        winners.append(winner)
        synopsises.append(synopsis)

        el = el.getnext()
        # save data to csv file
        fd.write(year + ',' + category + ',' + '"' + winner.encode('ascii', 'ignore') + '"' + ',' + synopsis.encode('ascii', 'ignore') + '\n')


fd.close()

# print data in pandas data frame in terminal
dic = {"Category": categories, "Winners": winners, "Synopsis": synopsises}
years = pandas.DataFrame(dic, index=years)
years.index.name="Years"
print years