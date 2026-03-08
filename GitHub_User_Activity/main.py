import json
import requests

print("Escriba su nombre de usuario: ")
username = str(input())

response = requests.get("https://api.github.com/users/{}/events".format(username))

if response.status_code == 200:
  data = json.loads(response.text)
  print(data)
