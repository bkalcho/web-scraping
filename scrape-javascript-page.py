#!/usr/bin/env python
__author__ = 'kalcho'
# Retrieve text behind the AJAX

from selenium import webdriver
import os
import time

phantomJSExecPath = os.getenv('HOMEPATH') + '\Desktop\phantomjs-2.1.1-windows\\bin\phantomjs.exe'
driver = webdriver.PhantomJS(executable_path=phantomJSExecPath)
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
time.sleep(3)
# Use BeautifuSoup for parsing instead of webdriver selectors
# pageSource = driver.page_source
# bsObj = BeautifulSoup(pageSource, "html.parser")
# print bsObj.find(attrs={"id":"content"}).get_text()
print driver.find_element_by_id('content').text
driver.close()