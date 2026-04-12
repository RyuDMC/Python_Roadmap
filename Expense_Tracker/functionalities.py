import os
import time
import json

filename = "/media/ryudmc/17bd76d4-00a3-4be2-a374-79313809c703/Oliver/Programing/Codes/Python/Python_Roadmap/Expense_Tracker/data.json"

def add(description, amount):
  if os.path.exists(filename) and os.path.getsize(filename) > 0:
    with open(filename, "r") as jsonfile:
      try:
        data = json.load(jsonfile)
      except:
        data = {"last_id" : 0, "expenses" : []}
  else:
    data = {"last_id" : 0, "expenses" : []}

  new_id = data["last_id"] + 1
  data["expenses"].append([new_id, time.ctime(), description, amount])
  data["last_id"] = new_id

  with open(filename, "w") as jsonfile:
    json.dump(data, jsonfile, indent = 2)
    print(data)

def update(id, amount):
  if os.path.exists(filename) and os.path.getsize(filename) > 0:
    with open(filename, "r") as jsonfile:
      data = json.load(jsonfile)

      data["expenses"][id - 1] = amount
      data["expenses"][id - 1][1] = time.ctime()
    with open(filename, "w") as jsonfile:
      json.dump(data, jsonfile, indent = 2)
  else:
    print("Error, Empty List")

def delete(id):
  if os.path.exists(filename) and os.path.getsize(filename) > 0:
    with open(filename, "r") as jsonfile:
      data = json.load(jsonfile)
      if data["expenses"][id - 1] in data["expenses"]:
        data["expenses"].remove(data["expenses"][id - 1])
        id = 0
        for i in data["expenses"]:
          id += 1
          i[0] = id
        data["last_id"] = id
      else:
        print("Invalid ID")

    with open(filename, "w") as jsonfile:
      json.dump(data, jsonfile, indent = 2)
      print(data)
  else:
    print("Error, Empty List")

##def show():
##  if os.path.exists(filename) and os.path.getsize(filename) > 0:
##    with open(filename, "r") as jsonfile:
      