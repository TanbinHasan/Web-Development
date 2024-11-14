food_list = [] # all foods will be stored here

while True:
  print("Favourite Foods Manager")
  print("0. Exit")
  print("1. Add foods")
  print("2. Remove foods")
  print("3. View favourite all foods")

  choice = int(input("Enter your choice: "))

  if choice == 0: # Exit part of the code
    print("Thanks for using Favourite Foods Manager")
    break

  if choice == 1: # add any item
    food = input("Enter one of your favorite meal name: ")
    if food in food_list: print(food + ", already exists in the list")
    else:
      food_list.append(food)
      print(food + ", has been added to the list")
  elif choice == 2: # remove any item
    if not food_list:
      print("The list is currently empty, therefore no items can be removed.")
      continue
    food = input("Enter a meal name to remove: ")
    if food not in food_list: print(food + ", does not exist in the list")
    else:
      food_list.remove(food)
      print(food + ", has been removed from the list successfully")
  elif choice == 3: # view the full list altogether
    if not food_list:
      print("List is empty to show anything.")
    else:
      for index, food in enumerate(food_list):
        print(index + 1, '.',  food)
  else: print("Invalid choice")