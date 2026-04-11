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
        resume[repo_name]["created_branch"] += 1
      elif created == "tag":
        resume[repo_name]["created_tag"] += 1
    elif tipo == "RemoveEvent":
      removed = evento["payload"].get("ref_type", "")
      if removed == "branch":
        resume[repo_name]["removed_branch"] += 1
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
  return resume

def show(resume):
  for repo, actions in resume.items():
    if actions.get("pushes"):
      print(f" - Pushed {actions["pushes"]} commits to {repo}")
    if actions.get("pull_request_opened"):
      print(f" - Opened {actions["pull_request_opened"]} pull requests in {repo}")
    elif actions.get("pull_request_closed"):
      print(f" - Closed {actions["pull_request_closed"]} pull requests in {repo}")
    elif actions.get("pull_request_merged"):
      print(f" - Merged {actions["pull_request_merged"]} pull requests in {repo}")
    elif actions.get("pull_request_reopend"):
      print(f" - Reopened {actions["pull_request_reopened"]} pull requests in {repo}")
    elif actions.get("pull_request_assigned"):
      print(f" - Assigned {actions["pull_request_assigned"]} pull requests in {repo}")
    elif actions.get("pull_request_labeled"):
      print(f" - Labeled {actions["pull_request_labeled"]} pull requests in {repo}")
    elif actions.get("pull_request_unassigned"):
      print(f" - Unassigned {actions["pull_request_unassigned"]} pull requests in {repo}")
    elif actions.get("pull_request_unlabeled"):
      print(f" - Unlabeled {actions["pull_request_unlabeled"]} pull requests in {repo}")
    if actions.get("commits"):
      print(f" - Pushed {actions["commits"]} commits to {repo}")
    if actions.get("stars"):
      print(f" - The repository {repo} received {actions["stars"]} stars")
    if actions.get("discussion"):
      print(f" - Created {actions["discussion"]} discussions in {repo}")
    if actions.get("IssueCommentEvent"):
      print(f" - Pushed {actions["issuecomment"]} issuecomments to {repo}")
    if actions.get("issues_opened"):
      print(f" - {actions["issues_opened"]} issues were opened in {repo}")
    if actions.get("issues_reopened"):
      print(f" - {actions["issues_reopened"]} issues were reopened in {repo}")
    if actions.get("issues_closed"):
      print(f" - {actions["issues_closed"]} issues were closed in {repo}")
    if actions.get("public"):
      print(f" - The repository {repo} became public")
    if actions.get("launched"):
      print(f" - The repository {repo} was launched")
    if actions.get("member"):
      print(f" - The repository {repo} has {actions["member"]}")
    if actions.get("created_branch"):
      print(f" - The repository {repo} has {actions["created_branch"]} branchs")
    if actions.get("created_tag"):
      print(f" - The repository {repo} has {actions["created_tag"]} tags")
    if actions.get("removed_branch"):
      print(f" - The repository {repo} removed {actions["removed_branch"]} branchs")
    if actions.get("created_page"):
      print(f" - The repository {repo} has {actions["created_page"]} pages created")
    if actions.get("edited_page"):
      print(f" - The repository {repo} has {actions["edited_page"]} pages edited")