#!/usr/bin/env python
__author__ = 'kalcho'

import requests

session = requests.Session()
params = {'username':'username', 'password':'password'}
s = session.post("http://pythonscraping.com/pages/cookies/welcome.php", data=params)
print "Cookie is set to:"
print s.cookies.get_dict()
print "--------------------"
print "Going to profile page..."
s = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print s.text