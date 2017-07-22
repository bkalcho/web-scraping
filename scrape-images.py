#!/usr/bin/env python
__author__ = 'kalcho'

import os
from urllib import urlopen, urlretrieve
from bs4 import BeautifulSoup


download_directory = "downloaded"
base_url = "http://pythonwebscraping.com"

def get_absolute_url(base_url, source):
    if source.startswith("http://www."):
        url = "http://" + source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = "http://" + source[4:]
    else:
        url = base_url + "/" + source
    
    if base_url not in url:
        return None
    return url


def get_download_path(base_url, absolute_url, download_dir):
    path = absolute_url.replace("www.", "")
    path = path.replace(base_url, "")
    path = download_directory + path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)
    
    return path


html = urlopen(base_url)
bsObj = BeautifulSoup(html, "html.parser")
download_list = bsObj.find_all(src=True)


for download in download_list:
    file_url = get_absolute_url(base_url, download["src"])
    if file_url is not None:
        print file_url

urlretrieve(file_url, get_download_path(base_url, file_url, download_directory))