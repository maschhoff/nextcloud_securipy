"""
Nextcloud Security Checker

settings - Helpers

2020 maschhoff github.com/maschhoff

"""

import json

def loadConfig():
    #print("loadConfig()")
    res={}
    with open('./data/config.json', 'r') as fp:
        res = json.load(fp)
    return res
