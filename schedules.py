#!/usr/local/bin/python3.5

import asyncio
from aiohttp import ClientSession
import json
from bs4 import BeautifulSoup

async def get_html(client, url):
	async with client.get("http://www.espn.com/mens-college-basketball/team/schedule/_/id/" + url) as res:
		return await res.read()

async def send_reqs(client, url, sem):
	with (await sem):
		res = await get_html(client, url)
	parse_html(res)

def parse_html(res):
	soup = BeautifulSoup(res, "html.parser")
	# gets all 'li'
	el = [i for i in soup.find_all('li')]
	# non_empty = [j for j in el if j.get('class') != []]
	# opp = [x for x in non_empty if 'team-name' in x.get('class')]
	print(non_empty)

if __name__ == "__main__":
	with open("espn_id.json") as file:
		team_id = json.load(file)
	with ClientSession() as session:
		sem = asyncio.Semaphore(100)
		loop = asyncio.get_event_loop()
		tasks = asyncio.wait([send_reqs(session, team_id[key], sem) for key in team_id])
		loop.run_until_complete(tasks)
