import json

def add(description, amount):
  with open("/media/ryudmc/17bd76d4-00a3-4be2-a374-79313809c703/Oliver/Programing/Codes/Python/Python_Roadmap/Expense_Tracker/data.json", "r+") as jsonfile:
    data = json.load(jsonfile)
    id = data["last_id"] + 1
    data["expenses"].extend([id, description, amount])
    data["last_id"] = id
    jsonfile.seek(0)
    json.dump(data, jsonfile)
    jsonfile.truncate()
