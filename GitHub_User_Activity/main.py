import json
import requests
from collections import defaultdict

print("Escriba su nombre de usuario: ")
username = str(input())

response = requests.get("https://api.github.com/users/{}/events/public".format(username))

if response.status_code == 200:
  eventos = json.loads(response.text)
  resume = defaultdict(lambda: defaultdict(int))

  from eventos import show as show
  from eventos import add_event as add_event
  add_event()
  show()
