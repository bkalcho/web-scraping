#!/usr/bin/env python
__author__ = 'kalcho'

import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth("Ryan", "password")
r = requests.post("http://pythonscraping.com/pages/auth/login.php", auth=auth)
print r.text