import requests
import json
import csv
import yaml
import warnings
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

f = open('http_profile.yml','r')
payloads = yaml.load(f)
f5device =  "192.168.2.66"
user = "admin"
password = "p@ssword123"



for payload in payloads:
  profile_name = payload['profile']
  profile_type = payload['type']
  p_att = payload['insertXforwardedFor']



headers = {'Content-type': 'application/json'}

profile_data = {"name":profile_name,"defaultsFrom":"/Common/"+profile_type,
                "insertXforwardedFor":p_att}

def create_profile():
  r = requests.post("https://"+f5device+"/mgmt/tm/ltm/profile/http", data=json.dumps(profile_data),auth=(user,password),headers=headers,verify=False)
  print(r.text)


print("creating profile")
create_profile()

