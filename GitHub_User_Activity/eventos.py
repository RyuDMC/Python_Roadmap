from main import resume as resume
from main import eventos as eventos
from main import response as response

def add_event():
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
      resume[repo_name]["create"] += [created]
    elif tipo == "RemoveEvent":
      removed = evento["ref_type"]
      resume[repo_name]["remove"] += [removed]
    elif tipo == "DiscussionEvent":
      resume[repo_name]["discussion"] += 1
    elif tipo == "GollumEvent":
      resume[repo_name]["page"] += 1
    elif tipo == "IssueCommentEvent":
      resume[repo_name]["issuecomment"] += 1
    elif tipo == "IssuesEvent":
      action = evento["action"]
      if action == "opened":
        resume[repo_name]["issues"]["opened"] += 1
      elif action == "closed":
        resume[repo_name]["issues"]["closed"] += 1
      else:
        response[repo_name]["issues"]["reopened"] += 1
    elif tipo == "MemberEvent":
      member = evento["member"]
      response[repo_name]["members"] += member
    elif tipo == "PublicEvent":
      resume[repo_name]["public"] = 1
    elif tipo == "LaunchEvent":
      resume[repo_name]["launched"] = 1
    else:
      print("Invalid Operation, ):")

def show():
  for repo, actions in resume.items():
    if actions.get("pushes"):
      print(f" - Pushed {actions["pushes"]} commits to {repo}")
    if actions.get("commits"):
      print(f" - Pushed {actions["commits"]} commits to {repo}")
    if actions.get("stars"):
      print(f" - {repo} received {actions["stars"]} stars")
    if actions.get("create"):
      for created in actions["create"]:
        print(f"The {created} was create in {repo}")
    if actions.get("remove"):
      for removed in actions["remove"]:
        print(f"The {removed} was remove from {repo}")
    if actions.get("DiscussionEvent"):
      print(f"Created {actions["discussion"]} discussions in {repo}")
    if actions.get("GollumEvents"):
      print(f"Created {actions["page"]} pages in {repo}")
    if actions.get("IssueCommentEvent"):
      print(f" - Pushed {actions["issuecomment"]} issuecomments to {repo}")
    if actions.get("issues"):
      print(f"{actions["issues"]["opened"]} had open in {repo}")
      print(f"{actions["issues"]["closed"]} had close in {repo}")
      print(f"{actions["issues"]["reopened"]} had reopen in {repo}")
    if actions.get("member"):
      for member in actions["members"]:
        print(f"added {member} to {repo}")
    if actions.get("public"):
      print(f"The {repo} became public")
    if actions.get("launched"):
      print(f"The {repo} was launched")
