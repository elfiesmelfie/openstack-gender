#!/usr/bin/env python
# matt@nycresistor.com - guesses gender count on openstack contributors

import gender
import json
import requests

release = 'kilo'
url = 'http://stackalytics.com/api/1.0/stats/engineers?release='
url += release
params = dict ()
resp = requests.get(url=url, params=params)
devs = json.loads(resp.text)

malecount = 0
femalecount = 0
unknowncount = 0

for developers in devs['stats']:
    name = developers['name']
    sname = name.split()
    fname = sname[0].upper()
    try:
        gendev = gender.gender[fname]
        if gendev == 'male' :
            malecount += 1
        else:
            femalecount += 1
    except:
            unknowncount += 1

print "females : %s" % femalecount
print "males : %s" % malecount
print "unknowncount : %s" %unknowncount 

