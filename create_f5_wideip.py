import requests
import json
import warnings
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

f5device =  "192.168.2.66"
user = "admin"
password = "p@ssword123"






headers = {'Content-type': 'application/json'}


dc_data = {"name":"India","enabled":True}
vs_data = {"name":"lab.localhost","enabled":True,"virtual-servers":[{'name':'test_vs','destination':'1.1.1.1:80'}],"addresses":['192.168.2.66'],"datacenter":"India"}
pool_data = {"name":"test_pool","enabled":True,"members":['lab.localhost:test_vs']}
wip_data = {"name":"test1.gtm.com","enabled":True,"pools":['test_pool']}

def create_dc():
  r = requests.post("https://"+f5device+"/mgmt/tm/gtm/datacenter", data=json.dumps(dc_data),auth=(user,password),headers=headers,verify=False)
  print(r.text)


def create_vs():
  r = requests.post("https://"+f5device+"/mgmt/tm/gtm/server", data=json.dumps(vs_data),auth=(user,password),headers=headers,verify=False)
  print(r.text)


def create_pool():
  r = requests.post("https://"+f5device+"/mgmt/tm/gtm/pool/a", data=json.dumps(pool_data),auth=(user,password),headers=headers,verify=False)
  print(r.text)


def create_wip():
  r = requests.post("https://"+f5device+"/mgmt/tm/gtm/wideip/a", data=json.dumps(wip_data),auth=(user,password),headers=headers,verify=False)
  print(r.text)

print("creating datacenter")
create_dc()
print("creating virtual server")
create_vs()
print("creating pool")
create_pool()
print("creating wideip")
create_wip()

