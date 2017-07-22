#!.usr.bin/env python
__author__ = 'kalcho'

import requests
import re
import string
from bs4 import BeautifulSoup
from collections import OrderedDict, defaultdict, Counter


def clean_input(input):
    input = input.upper()
    input = re.sub('\n+', " ", input)
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    input = bytes(input).decode(encoding='utf-8')
    input = input.encode(encoding='ascii', errors='ignore')
    clean_input = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            clean_input.append(item)
    return clean_input


def ngrams(input, n):
    input = clean_input(input)
    output = []
    for i in xrange(len(input)-n+1):
        output.append(input[i:i+n])
    return output


response = requests.get("http://en.wikipedia.org/wiki/Python_(programming_language")
bsObj = BeautifulSoup(response.content, "html.parser")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
ngrams1 = ngrams(content, 2)
ngrams = defaultdict(int)
for k in ngrams1:
    ngrams[str(k)] += 1 
ngrams = OrderedDict(sorted(ngrams.items(), key=(lambda t: t[1]), reverse=True))
print ngrams
print "\nTotal number of 2-grams is: %d\nNumber of unique 2-grams is: %d" \
        % (len(ngrams1), len(ngrams))