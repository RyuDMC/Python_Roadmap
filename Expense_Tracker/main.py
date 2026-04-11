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
elif option == 2:
  print("Select expense's ID: ")
  ID = int(input())
  print("Define new amount: ")
  amount = int(input())

  from functionalities import update
  update(ID, amount)
elif option == 3:
  print("Select expense's ID: ")
  ID = int(input())

  from functionalities import delete
  delete(ID)
