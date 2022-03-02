#!/usr/bin/env python3

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import requests from xml.etree import ElementTree

def toolkit_get_cve(cve, token):
    URL = "https://gistoolkit..com/V1/Vulnerabilities/" +cve
    headers = {"toolkit-token": token}

    req = requests.get(url = URL, headers = headers, verify=False)
    #print('GIS TOOL KIT URL: ', URL)
 #print('req.status_code: ',req.status_code)  if 200 != req.status_code :
        print('Exiting due to invalid Toolkit request for CVE ' + cve )
        return 'None'

 tree = ElementTree.fromstring(req.content)
    #print(ElementTree.tostring(tree))
  rating = tree.find('analysis').find('AnalysisResponse').find('rating')
    if rating == None :
        print('GIS toolkit return None')
        return ''
 print('**** CVE: ' + cve)
 print(' Rating: ' + rating.text) return rating.text
