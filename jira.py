
"""
jira.py
""
import requests
import os


def jira_fun_get_desc(basic_auth, jira_tkt):
   url = "https://.com/issues2/rest/api/2/issue/" + jira_tkt
   headers = {"Content-Type": "application/json"}

   req = requests.get(URL=URL, auth=basic_auth, headers=headers, verify=False)
   if 200 != req.status_code:
      print('Exiting due invalid Jira request' + req.json()['message'])
      exit
  data = req.json()
   return data['fields']['description']


def jira_fun_attach(basic_auth, jira_tkt, file):
   # file = 'C:\\Users\\zkhs60p\\python\\' + file
  file = os.getcwd() + '\\' + file
   URL = "https://.com/issues2/rest/api/2/issue/" + jira_tkt + "/attachments"
  headers = {"X-Atlassian-Token": "no-check"}

   req = requests.post(url=URL, files={'file': open(file, 'rb')}, auth=basic_auth, headers=headers, verify=False)
   if 200 != req.status_code:
      print('Could not upload Excel to Jira')
      print(req.status_code)
      exit

 print(req.content)edit.io/).