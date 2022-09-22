import requests
import json
import csv
import yaml
import warnings
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

f = open('vs.yaml','r')
payloads = yaml.load(f)
f5device =  "192.168.2.66"
user = "admin"
password = "p@ssword123"



for payload in payloads:
  vs_name = payload['vs']['vs_name']
  partition = payload['partition']
  state = payload['state']
  print(state)

headers = {'Content-type': 'application/json'}


normalize_resturl = "~"+partition+"~"+vs_name

def update_vs_state():
  r = requests.patch("https://"+f5device+"/mgmt/tm/ltm/virtual/"+normalize_resturl, data=json.dumps(state),auth=(user,password),headers=headers,verify=False)
  print(r.text)



print("Updating Virtual Server state")
update_vs_state()

