#!/usr/bin/env python
__author__ = 'kalcho'
# Get Nobel prize winners by year and category

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


driver = webdriver.PhantomJS(executable_path=(os.getenv('HOMEPATH') + '\Desktop\phantomjs-2.1.1-windows\\bin\phantomjs.exe'))
driver.get('http://www.nobelprize.org/nobel_prizes/lists/all/index.html')
middle_row = driver.find_element(By.ID, "nobel-middle-col")
title = middle_row.find_element(By.XPATH, "./div/div/h1").text
prizes_info = middle_row.find_elements_by_css_selector(".by_year")
for prize_info in prizes_info:
    print prize_info.find_element_by_xpath(".//h3").text.encode('utf-8')
    print prize_info.find_element_by_xpath(".//h6").text.encode('utf-8')
    print prize_info.find_element_by_xpath(".//p").text.encode('utf-8') + '\n'
driver.close()