import json
import requests

print("Escriba su nombre de usuario: ")
username = str(input())

response = requests.get("https://api.github.com/users/{}/events/public".format(username))

if response.status_code == 200:
  with open("/media/ryudmc/17bd76d4-00a3-4be2-a374-79313809c703/Oliver/Programing/Codes/Python/Python_Roadmap/GitHub_User_Activity/data.json", "w") as new_data:
    data = json.dumps(json.loads(response.text))
    json.dump(data, new_data)