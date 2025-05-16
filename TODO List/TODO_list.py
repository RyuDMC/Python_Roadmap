import os
import sys
import time
import json
import actions

try: 
  order = sys.argv[1]

  if ("show" in order) == False:
    task_id = sys.argv[2]
  if order == "add":
    task_description = sys.argv[2]
  if order == "update":
    task_description = sys.argv[3]
except IndexError:
  order = "help"

if(order == "help"):
  print("""TODO list is a minimalistic TODO list app for linux terminal 
  Usage:
      python3 TODO-list.py [command] [..args]      

  Aviable commans:
      add [text] - add the text, status to the TODO List
      remove [num] - remove the text to the TODO list, if no text is found, do nothing
      update [num] [text] - update the selected task
      mark_in_progress [num] - mark the task num how in-progress
      mark_done [num] - mark the task num how done
      show_all - print all tasks
      show_done - print all done tasks
      show_todo - print all todo tasks
      show_in_progress - print all in-progress tasks
        
  Important info.... maybe):
      the status of tasks are: 
        0 -> not done
        1 -> in progress
        2 -> done
""")
  exit()

if os.stat("Tasks.json").st_size != 0:
  with open("Tasks.json", "r") as tasks:
    actions.dict_json = json.load(tasks)

with open("Tasks.json", "w") as tasks:
  if order == "add":
    actions.add(task_description, 0)
  if order == "remove":
    actions.remove(task_id)
  if order == "update":
    actions.update(task_id, task_description)
  if order == "mark_in_progress":
    actions.mark_in_progress(task_id)
  if order == "mark_done":
    actions.mark_done(task_id)
  if order == "show_all":
    actions.show_all()
  if order == "show_todo":
    actions.show_todo()
  if order == "show_in_progress":
    actions.show_in_progress()  
  if order == "show_done":
    actions.show_done()
  
  json.dump(actions.dict_json, tasks)