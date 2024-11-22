import CRUD
import View_Books

# Load books from CSV when the program starts
CRUD.load_books()

while True:
  print("Welcome to Library Management System")
  print("0. Exit")
  print("1. Add Books")
  print("2. Remove Book")
  print("3. Update Book")
  print("4. View All Books")

  menu = int(input("Enter your choice: "))

  if menu == 0:
    print("Thank you for using Library Management System")
    break
  elif menu == 1: CRUD.add()
  elif menu == 2: CRUD.remove()
  elif menu == 3: CRUD.update()
  elif menu == 4: View_Books.view_all_books()
  else: print("Choose a valid option.")