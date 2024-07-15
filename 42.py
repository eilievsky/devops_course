import requests
import pprint
import json


#response = requests.get("https://api.github.com/users/eilievsky/repos")

response = requests.get("https://fake-json-api.mock.beeceptor.com/companies")

if response.status_code == 200:
    print(response.json())
    # repos = json.loads(response.json())
    repos = response.json()
    for repo in repos:
        print(repo['name'])


