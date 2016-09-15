#!/usr/local/bin/python3.5
'''
	gets and exports the ids of all the teams from ESPN
'''

from bs4 import BeautifulSoup
import urllib.request
import json

url = "http://www.espn.com/mens-college-basketball/standings"
content = urllib.request.urlopen(url).read()
soup = BeautifulSoup(content, "html.parser")

team_id = {}
links = [x.get('href') for x in soup.find_all('a')]
teams = [i for i in links if "http://www.espn.com/mens-college-basketball/team/_/id/" in i]

for t in teams:
	name = t.split('/')[-1]
	_id = t.split('/')[-2]
	team_id[str(name)] = str(_id)

with open("espn_id.json", "w") as out:
	out.write(json.dumps(team_id))