import argparse

parse = argparse.ArgumentParser(description = "Expense Tracker")
subparsers = parse.add_subparsers(dest = "command", help = "available commands")

#command add
parse_add = subparsers.add_parser("add", help = "add expense")
parse_add.add_argument("--description", type = str, help = "expense's description")
parse_add.add_argument("--amount", type = int, help = "amount")

#command update
parse_update = subparsers.add_parser("update", help = "update expense")
parse_update.add_argument("--ID", type = int)
parse_update.add_argument("--amount", type = int)

#command delete
parse_delete = subparsers.add_parser("delete", help = "delete expense")
parse_delete.add_argument("--ID", type = int)

#command list
parse_list = subparsers.add_parser("list", help = "show all expenses")

#command summary
parse_summary = subparsers.add_parser("summary", help = "show summary of expense")
parse_summary.add_argument("--mount", type = str)

args = parse.parse_args()

if args.command == "add":
  if args.amount < 0:
    print("Invalid amount")
  else:
    from functionalities import add
    add(args.description, args.amount)

elif args.command == "update":
  if args.amount < 0:
    print("Invalid amount")
  else:
    from functionalities import update
    update(args.ID, args.amount)

elif args.command == "delete":
  from functionalities import delete
  delete(args.ID)

elif args.command == "list":
  from functionalities import show
  show()

elif args.command == "summary":
  if args.mount:
    from functionalities import month_summary
    month_summary(args.month)
  else: 
    from functionalities import summary
    summary()