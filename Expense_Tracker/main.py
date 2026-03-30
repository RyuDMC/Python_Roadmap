import json

with open("/media/ryudmc/17bd76d4-00a3-4be2-a374-79313809c703/Oliver/Programing/Codes/Python/Python_Roadmap/Expense_Tracker/data.json", "r+") as jsonfile:
  json.dump({"last_id" : 0, "expenses" : []}, jsonfile)

from functionalities import add

add("test", 20)

with open("/media/ryudmc/17bd76d4-00a3-4be2-a374-79313809c703/Oliver/Programing/Codes/Python/Python_Roadmap/Expense_Tracker/data.json", "r+") as jsonfile:
  print(jsonfile)

add("test2", 50)

with open("/media/ryudmc/17bd76d4-00a3-4be2-a374-79313809c703/Oliver/Programing/Codes/Python/Python_Roadmap/Expense_Tracker/data.json", "r+") as jsonfile:
  print("ID Description Amount")
