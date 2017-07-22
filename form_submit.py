#!/usr/bin/env python
__author__ = 'kalcho'

import requests


params = {"firstname": "Ryan", "lastname": "Mitchell"}
r = requests.post("http://pythonscraping.com/pages/files/processing.php", data=params)
print r.text