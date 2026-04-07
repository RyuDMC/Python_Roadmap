import os
import json


print("Select your operation: \n")
print("1/ Add\n2/ Update\n3/ Delete\n4/ Show_All\n5/ Summary\n6/ Especific_Summary")

option = int(input())

if option == 1:
  print("Define your expense: ")
  input = str(input()).split()
  description = str(input[0])
  amount = int(input[1])
  
  from functionalities import add
  add(description, amount)