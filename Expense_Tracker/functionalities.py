import os
import json


def add(description, amount):
  filename = "/media/ryudmc/17bd76d4-00a3-4be2-a374-79313809c703/Oliver/Programing/Codes/Python/Python_Roadmap/Expense_Tracker/data.json"

  if os.path.exists(filename) and os.path.getsize(filename) > 0:
    with open(filename, "r") as jsonfile:
      try:
        data = json.load(jsonfile)
      except:
        data = {"last_id" : 0, "expenses" : []}
  else:
    data = {"last_id" : 0, "expenses" : []}

  new_id = data["last_id"] + 1
  data["expenses"].append([new_id, description, amount])
  data["last_id"] = new_id

  with open(filename, "w") as jsonfile:
    json.dump(data, jsonfile, indent = 2)
  
  print(data)