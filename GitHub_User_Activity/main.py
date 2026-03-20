import json
import requests


username = "VIRUSGAMING64"

response = requests.get("https://api.github.com/users/{}/events/public".format(username))

if response.status_code == 200:
  eventos = json.loads(response.text)

  from aux_functions import show
  from aux_functions import add_event
  add_event()
  show()
