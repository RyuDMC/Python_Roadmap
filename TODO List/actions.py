import time
import json

dict_json = dict()
dict_json["counter"] = 0
dict_json["dict_tasks"] = dict()

def dumper():
  with open("Tasks.json", "w") as tasks:
    json.dump(dict_json, tasks)

def add(description, status):
  id = dict_json["counter"]
  new_task = list([description, int(status), time.ctime(), time.ctime()])
  dict_json["dict_tasks"][id] = new_task
  dict_json["counter"] += 1
  print("Task added successfully ID = {}".format(id))

def remove(id):
  if dict_json["dict_tasks"].get(id) == None:
    print("Invalid operation, try again")
    dumper()
    exit()
  else:
    dict_json["dict_tasks"].pop(id)

def update(id, description):
  if dict_json["dict_tasks"].get(id) == None:
    print("Invalid operation, try again")
    dumper()
    exit()
  else:
    dict_json["dict_tasks"][id][0] = description
    dict_json["dict_tasks"][id][3] = time.ctime()


def mark_in_progress(id):
  if dict_json["dict_tasks"].get(id) == None:
    print("Invalid operation, try again")
    dumper()
    exit()
  else:
    dict_json["dict_tasks"][id][1] = 1

def mark_done(id):
  if dict_json["dict_tasks"].get(id) == None:
    print("Invalid operation, try again")
    dumper()
    exit()
  else:
    dict_json["dict_tasks"][id][1] = 2

def show(index):
  print(dict_json["dict_tasks"][index][0], end=" ")
  print(dict_json["dict_tasks"][index][1], end=" ")
  print(dict_json["dict_tasks"][index][2], end=" ")
  print(dict_json["dict_tasks"][index][3])

def show_all():
  for i in dict_json["dict_tasks"]:
    print(i, end=" ")
    show(i)

def show_todo():
  for i in dict_json["dict_tasks"]:
    if dict_json["dict_tasks"][i][1] == 0:
      print(i, end=" ")
      show(i)

def show_in_progress():
  for i in dict_json["dict_tasks"]:
    if dict_json["dict_tasks"][i][1] == 1:
      print(i, end=" ")
      show(i)

def show_done():
  for i in dict_json["dict_tasks"]:
    if dict_json["dict_tasks"][i][1] == 2:
      print(i, end=" ")
      show(i)
