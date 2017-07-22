#!/usr/bin/env python
__author__ = 'kalcho'

from urllib2 import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import pymysql
import re


conn = pymysql.connect(host="127.0.0.1", user="root", passwd="", db="mysql", charset="utf8")
cur = conn.cursor()
cur.execute("USE scraping")

random.seed(datetime.datetime.now())

def store(title, content):
    cur.execute("INSERT INTO pages (title, content) VALUES (\"%s\", \"%s\")", (title, content))
    cur.connection.commit()


def get_links(article_url):
    html = urlopen("https://en.wikipedia.org"+article_url)
    bsObj = BeautifulSoup(html, "html.parser")
    title = bsObj.find("h1").get_text()
    content = bsObj.find("div", {"id": "mw-content-text"}).find("p").get_text()
    store(title, content)
    return bsObj.find("div", {"id": "bodyContent"}).find_all("a", href=re.compile("(^/wiki/)((?!:).)*$"))


links = get_links("/wiki/Kevin_Bacon")
try:
    while len(links) > 0:
        new_article = links[random.randint(0, len(links)-1)].attrs["href"]
        print new_article
        links = get_links(new_article)

finally:
    cur.close
    conn.close()