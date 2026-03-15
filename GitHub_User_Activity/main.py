import json
import requests
from collections import defaultdict

print("Escriba su nombre de usuario: ")
username = str(input())

response = requests.get("https://api.github.com/users/{}/events/public".format(username))

if response.status_code == 200:
  eventos = json.loads(response.text)
  resume = defaultdict(lambda: defaultdict(int))

  for evento in eventos:
    tipo = evento["type"]
    repo_name = evento["repo"]["name"]

    if tipo == "PushEvent":
      resume[repo_name]["pushes"] += 1
    elif tipo == "PullRequestEvent":
      resume[repo_name]["pulls"] += 1
    elif tipo == "WatchEvent":
      resume[repo_name]["stars"] += 1
    elif tipo == "CommitCommentEvent":
      resume[repo_name]["commits"] += 1
    elif tipo == "CreateEvent":
      created = evento["ref_type"]
      resume[repo_name]["create"][created] += 1
    elif tipo == "RemoveEvent":
      removed = evento["ref_type"]
      resume[repo_name]["remove"][removed] += 1
    elif tipo == "DiscussionEvent":
      resume[repo_name]["discussion"] += 1
      