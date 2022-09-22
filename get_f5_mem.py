import requests
import json
import csv
import yaml
import warnings
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

f5device =  "192.168.2.66"
user = "admin"
password = "p@ssword123"




headers = {'Content-type': 'application/json'}



def get_mem():
  memdata = {}
  r = requests.get("https://"+f5device+"/mgmt/tm/sys/memory", auth=(user,password),headers=headers,verify=False)
  values = r.json()
  for x in values['entries']:
    if 'memory-host' in x :
      for y in values['entries'][x]['nestedStats']['entries']:
        tmmMemoryFree = values['entries'][x]['nestedStats']['entries'][y]['nestedStats']['entries']['tmmMemoryFree']['value']
        tmmMemoryTotal= values['entries'][x]['nestedStats']['entries'][y]['nestedStats']['entries']['tmmMemoryTotal']['value']
        tmmMemoryUsed = values['entries'][x]['nestedStats']['entries'][y]['nestedStats']['entries']['tmmMemoryUsed']['value']               
  memdata['tmmMemoryFree']=tmmMemoryFree
  memdata['tmmMemoryTotal']=tmmMemoryTotal
  memdata['tmmMemoryUsed']=tmmMemoryUsed
  return memdata
print("getting mem")
data = get_mem()
print(data)
