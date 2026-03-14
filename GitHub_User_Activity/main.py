import json
import requests
from collections import defaultdict

print("Escriba su nombre de usuario: ")
username = str(input())

response = requests.get("https://api.github.com/users/{}/events/public".format(username))

if response.status_code == 200:
  data = json.loads(response.text)
  resume = defaultdict(lambda: defaultdict(int))