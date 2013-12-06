#!/usr/bin/python

import json
import urllib2

# get the top headline from redit
url = 'http://reddit.com/.json?limit=1'
_user_agent = 'Get Reddit Top Headline by Kristas @ github.com/kristas'
_request = urllib2.Request(url, headers={'User-agent': _user_agent})
_json = json.loads(urllib2.urlopen(_request).read())
headline = _json['data']['children'][0]['data']['title']

# print out the html
print 'Content-type: text/xml'
print
print '<?xml version="1.0" encoding="UTF-8"?>'
print '<Response>'
print '<Say voice="alice">'
print headline
print '</Say>'
print '</Response>'
