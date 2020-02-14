"""
Nextcloud Security Checker

2020 maschhoff github.com/maschhoff

"""


import requests
import settings
import json
import noti

config=settings.loadConfig()

def check(url):
	
	# Request POST https://scan.nextcloud.com/api/queue
	
	data_send = {"url":url}
	se=requests.post('https://scan.nextcloud.com/api/queue', data=json.dumps(data_send), headers={'X-CSRF': 'true', 'Content-Type': 'application/json'})
	se=se.json() 
	
	# Request GET https://scan.nextcloud.com/api/result/ UUID
	
	res=requests.get('https://scan.nextcloud.com/api/result/'+se["uuid"], data="", headers={'X-CSRF': 'true', 'Content-Type': 'application/json'})
	res=res.json()
	
	# Notify
	
	if res["rating"]<4:
		noti.notifyAll("Rating down to: "+res["rating"])
	if len(res["vulnerabilities"])>0:
		noti.notifyAll("vulnerabilities found "+len(res["vulnerabilities"]))

check(config["url"])