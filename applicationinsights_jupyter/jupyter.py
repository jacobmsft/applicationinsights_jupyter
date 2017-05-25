import requests
import json

from datetime import datetime
from operator import itemgetter

baseurl = 'https://api.applicationinsights.io/beta/apps/{0}/query'
data = '{"query" : "{0}"}'
headers = {'x-api-key': '{0}', 'Content-Type': 'application/json'}

def connect(appId, apiKey):
    baseurl = baseurl.format(appId);
    headers = headers['x-api-key'].format(apiKey);

def execute(userQuery):
    query = data.format(userQuery)
    response = requests.post(url, headers=headers, data=data)
    if response != None && response.text != None && response.status_code == 200:
        jsonObj = json.loads(response.text)
        if jsonObj["Tables"] != None &&
            jsonObj["Tables"][0] != None &&
            jsonObj["Tables"][0]["Rows"] != None &&
            jsonObj["Tables"][0]["Columns"] != None
                rows = jsonObj["Tables"][0]["Rows"]
                columns = jsonObj["Tables"][0]["Columns"]



