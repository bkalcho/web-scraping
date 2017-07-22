#!/usr/bin/env python
__author__ = 'kalcho'

import requests

params = {"username":"Ryan", "password":"password"}

r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", data=params)
print "Cookie is set to:"
print r.cookies.get_dict()
print "-------------------"
print "Going to profile page..."
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)
print r.text