from library_manager import LibraryManager

def main():
  library = LibraryManager("stored_books.json")

  while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Update Book")
    print("4. Remove Book")
    print("5. Lend Book")
    print("6. Return Book")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ").strip()

    if choice == '1':
      print("\nAdd Book")
      title = input("Enter Book Title: ")
      author = input("Enter Author Name: ")
      year = int(input("Enter Publishing Year: "))
      price = float(input("Enter Book Price: "))
      quantity = int(input("Enter Quantity: "))
      if library.add_book(title, author, year, price, quantity):
        print("\nBook added successfully.")
      else:
        print("\nBook already exists, quantity updated.")
    
    elif choice == '2':
      print("\nView All Books")
      library.view_all_books()
    
    elif choice == '3':
      print("\nUpdate Book")
      isbn = int(input("Enter ISBN to update: "))
      title = input("Enter new Title (or leave empty to skip): ")
      author = input("Enter new Author (or leave empty to skip): ")
      year = input("Enter new Year (or leave empty to skip): ")
      price = input("Enter new Price (or leave empty to skip): ")
      quantity = input("Enter new Quantity (or leave empty to skip): ")
      library.update_book(isbn, title or None, author or None, year or None, price or None, int(quantity) if quantity else None)

    elif choice == '4':
      print("\nRemove Book")
      isbn = int(input("Enter ISBN to remove: "))
      library.remove_book(isbn)
    
    elif choice == '5':
      print("\nLend Book")
      isbn = int(input("Enter ISBN to lend: "))
      borrower_name = input("Enter Borrower's Name: ")
      borrower_phone = input("Enter Borrower's Phone Number: ")
      due_date = input("Enter Due Date (YYYY-MM-DD): ")
      library.lend_book(isbn, borrower_name, borrower_phone, due_date)
    
    elif choice == '6':
      print("\nReturn Book")
      isbn = int(input("Enter ISBN to return: "))
      library.return_book(isbn)
    
    elif choice == '7':
      print("\nSaving and Exiting...")
      library.save()
      print("Books saved. Exiting...\n")
      break
    
    else:
      print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
  main()