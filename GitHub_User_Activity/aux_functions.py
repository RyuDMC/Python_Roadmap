from collections import defaultdict

def add_event(eventos):
  resume = defaultdict(lambda: defaultdict(int))

  for evento in eventos:
    tipo = evento["type"]
    repo_name = evento["repo"]["name"]

    if tipo == "PushEvent":
      resume[repo_name]["pushes"] += 1
    elif tipo == "PullRequestEvent":
      action = evento["payload"].get("action", "")
      if action == "opened":
        resume[repo_name]["pull_request_opened"]+= 1
      elif action == "closed":
        resume[repo_name]["pull_request_closed"] += 1
      elif action == "merged":
        resume[repo_name]["pull_request_merged"] += 1
      elif action == "reopened":
        resume[repo_name]["pull_request_reopened"] += 1
      elif action == "assigned":
        resume[repo_name]["pull_request_assigned"] += 1
      elif action == "unassigned":
        resume[repo_name]["pull_request_unassigned"] += 1
      elif action == "labeled":
        resume[repo_name]["pull_request_labeled"] += 1
      elif action == "unlabeled":
        resume[repo_name]["pull_request_unlabeled"] += 1
    elif tipo == "WatchEvent":
      resume[repo_name]["stars"] += 1
    elif tipo == "CommitCommentEvent":
      resume[repo_name]["commits"] += 1
    elif tipo == "CreateEvent":
      created = evento["payload"].get("ref_type", "")
      if created == "branch":
        resume[repo_name]["branch"] += 1
      elif created == "repository":
        resume[repo_name]["repository"] += 1
      elif created == "tag":
        resume[repo_name]["tag"] += 1
    elif tipo == "RemoveEvent":
      removed = evento["payload"].get("ref_type", "")
      if removed == "branch":
        resume[repo_name]["branch"] += 1
      elif removed == "repository":
        resume[repo_name]["repository"] += 1
    elif tipo == "EventDiscussion":
      resume[repo_name]["discussion"] += 1
    elif tipo == "GollumEvent":
      action = evento["pages"].get("action", "")
      if action == "created":
        resume[repo_name]["created_page"] += 1
      elif action == "edited":
        resume[repo_name]["edited_page"] += 1
    elif tipo == "IssueCommentEvent":
      resume[repo_name]["issuecomment"] += 1
    elif tipo == "IssuesEvent":
      action = evento["payload"].get("ref_type", "")
      if action == "opened":
        resume[repo_name]["issues_opened"] += 1
      elif action == "closed":
        resume[repo_name]["issues_closed"] += 1
      else:
        resume[repo_name]["issues_reopened"] += 1
    elif tipo == "PublicEvent":
      resume[repo_name]["public"] = 1
    elif tipo == "LaunchEvent":
      resume[repo_name]["launched"] = 1
    elif tipo == "ForkEvent":
      resume[repo_name]["forked"] += 1
    elif tipo == "MemberEvent":
      resume[repo_name]["member"] += 1
    else:
      print(tipo)
  return resume

def show(resume):
  for repo, actions in resume.items():
    if actions.get("pushes"):
      print(f" - Pushed {actions["pushes"]} commits to {repo}")
    if actions.get("pull_request"):
      print(f" - Opened{actions["pull_request_opened"]} pull requests in {repo}")
      print(f" - Closed{actions["pull_request_closed"]} pull requests in {repo}")
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
