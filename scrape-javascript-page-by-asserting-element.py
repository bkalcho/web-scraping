#!/usr/bin/env python
__author__ = 'kalcho'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


driver = webdriver.PhantomJS(executable_path=(os.getenv('HOMEPATH') + '\Desktop\phantomjs-2.1.1-windows\\bin\phantomjs.exe'))
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loadedButton")))
finally:
    print driver.find_element_by_id("content").text
    driver.close()