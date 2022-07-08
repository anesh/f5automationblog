import requests
import json
import csv
import yaml
import warnings
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

f = open('VS_Data.yml','r')
payloads = yaml.load(f)
f5device =  "192.168.2.66"
user = "admin"
password = "p@ssword123"



for payload in payloads:
  vip_name = payload['VIP_NAME']
  vip = payload['VIP']
  c_profile= payload['CLIENT_PROFILe']
  s_profile = payload['SERVER_PROFILE']
  snat = payload['SNAT']
  pool_name = payload['pool']['pool_name']
  pool_mname = payload['pool']['member_name']
  pool_maddr = payload['pool']['member_address']
  partition = payload['partition']
  monitor = payload['monitor']['monitor_name']  
  mtype = payload['monitor']['MONITOR_TYPE']
  mint = payload['monitor']['interval']
  mout = payload['monitor']['timeout']
  msend = payload['monitor']['send']



headers = {'Content-type': 'application/json'}



vs_data = {"name":vip_name,"destination":vip,
        "mask":"255.255.255.255","source":"0.0.0.0/0",
        "profiles":[{"name":c_profile,"context":"clientside"},
                    {"name":s_profile,"context":"serverside"}],
        "sourceAddressTranslation":{"type":snat},
        "pool":pool_name}

pool_data = {"name":pool_name,"partition":partition,"monitor":"/Common/"+monitor,
             "members":[{"name":pool_mname,"address":pool_maddr}]}

monitor_data = {"name":monitor,"partition":partition,"defaultsFrom":"/Common/"+mtype,
                "destination":"*.*","interval":mint,"timeout":mout,"send":msend}

def create_monitor():
  r = requests.post("https://"+f5device+"/mgmt/tm/ltm/monitor/http", data=json.dumps(monitor_data),auth=(user,password),headers=headers,verify=False)
  print(r.text)


def create_pool():
  r = requests.post("https://"+f5device+"/mgmt/tm/ltm/pool", data=json.dumps(pool_data),auth=(user,password),headers=headers,verify=False)
  print(r.text)


def create_vs():
  r = requests.post("https://"+f5device+"/mgmt/tm/ltm/virtual", data=json.dumps(vs_data),auth=(user,password),headers=headers,verify=False)
  print(r.text)

print("creating monitor")
create_monitor()
print("creating pool")
create_pool()
print("creating virtual server")
create_vs()

