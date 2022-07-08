import requests
import json
import csv
import yaml
import warnings
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

f = open('pool_add.yml','r')
payloads = yaml.load(f)
f5device =  "192.168.2.66"
user = "admin"
password = "p@ssword123"



for payload in payloads:
  pool_name = payload['pool']['pool_name']
  pool_mname = payload['pool']['member_name']
  pool_maddr = payload['pool']['member_address']
  partition = payload['partition']



headers = {'Content-type': 'application/json'}

pool_data = {"name":"/Common/"+pool_mname,"address":pool_maddr}


def add_pool_members():
  r = requests.post("https://"+f5device+"/mgmt/tm/ltm/pool/"+pool_name+"/members", data=json.dumps(pool_data),auth=(user,password),headers=headers,verify=False)
  print(r.text)



print("Adding pool members")
add_pool_members()

