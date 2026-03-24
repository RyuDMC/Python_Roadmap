import json
import requests

print("Inserte nombre de usuario: ")
username = str(input())

response = requests.get("https://api.github.com/users/{}/events/public".format(username))

if response.status_code == 200:
  from aux_functions import show
  from aux_functions import add_event
  
  resume = add_event(eventos= json.loads(response.text))
  show(resume)
elif response.status_code == 301:
  print("The info had moved to another URL")
elif response.status_code == 403:
  print("The requested info is forbidden")
elif response.status_code == 404:
  print("Info not found")
else:
  print("Something goes wrong, try it again")