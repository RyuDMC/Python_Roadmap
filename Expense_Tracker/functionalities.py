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
        data = {"last_id" : 0, "expenses" : [], "max_description_size" : 11, "budget" : {}}
  else:
    data = {"last_id" : 0, "expenses" : [], "max_description_size" : 11, "budget": {}}

  new_id = data["last_id"] + 1
  data["last_id"] = new_id
  data["expenses"].append([new_id, time.ctime(), description, amount])
  data["max_description_size"] = len(description)
  
  with open(filename, "w") as jsonfile:
    json.dump(data, jsonfile, indent = 2)


def update(id, amount):
  if os.path.exists(filename) and os.path.getsize(filename) > 0:
    with open(filename, "r") as jsonfile:
      data = json.load(jsonfile)
      try:
        data["expenses"][id - 1] in data["expenses"]
      except IndexError:
        print("Invalid ID")
        return
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
      try:
        data["expenses"][id - 1] in data["expenses"]
      except IndexError:
        print("Invalid ID")
        return
      if data["expenses"][id - 1] in data["expenses"]:
        data["expenses"].remove(data["expenses"][id - 1])
        id = 0
        for i in data["expenses"]:
          id += 1
          i[0] = id
        data["last_id"] = id
        data["max_description_size"] = max(data["max_description_size"], len(i[2]))
    with open(filename, "w") as jsonfile:
      json.dump(data, jsonfile, indent = 2)
  else:
    print("Error, Empty List")

def show():
  if os.path.exists(filename) and os.path.getsize(filename) > 0:
    with open(filename, "r") as jsonfile:
      data = json.load(jsonfile)
      blank_spaces = data["max_description_size"] - 10
      print(f"ID time {19 * " "} Description{blank_spaces * " "}Expense")
      for items in data["expenses"]:
        sub_blank_spaces = 1
        if len(items[2]) > 11:
          sub_blank_spaces = len(items[2]) - blank_spaces - 9
        else:
          sub_blank_spaces = blank_spaces + 11 - len(items[2])
        print(f"{items[0]}  {items[1]} {items[2]}{sub_blank_spaces * " "}{items[3]}")
  else:
    print("Error, Empty List")
        
def summary():
  if os.path.exists(filename) and os.path.getsize(filename) > 0:
    total_sum = 0
    with open(filename, "r") as jsonfile:
      data = json.load(jsonfile)

      for items in data["expenses"]:
        total_sum += items[3]
    return total_sum
  else:
    print("Error, Empty List")

def month_summary(month_name):
  if os.path.exists(filename) and os.path.getsize(filename) > 0:
    total_sum = 0
    with open(filename, "r") as jsonfile:
      data = json.load(jsonfile)
      if len(month_name) > 3:
        month_name = month_name[:3]
      
      for items in data["expenses"]:
        month = items[1].split()[1]
        if month_name == month:
          total_sum += items[3]
    return total_sum
  else:
    print("Error, Empty List")

def set_budget(month_name, amount):
  if os.path.exists(filename) and os.path.getsize(filename) > 0:
    with open(filename, "r") as jsonfile:
      data = json.load(jsonfile)
      data["budget"][month_name[:3]] = amount
    
    with open(filename, "w") as jsonfile:
      json.dump(data, jsonfile, indent = 2)
  else:
    print("Error, Empty List")

def check_budget():
  month = time.ctime().split()[1]
  if os.path.exists(filename) and os.path.getsize(filename) > 0:
    with open(filename, "r") as jsonfile:
      data = json.load(jsonfile)
      if month in data["budget"]:
        amount = month_summary(month)
        if amount > data["budget"][month]:
          print(f"Month budget exceded")