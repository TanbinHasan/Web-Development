from library_manager import LibraryManager
from validation import validate_year, validate_price, validate_quantity, validate_isbn, validate_date

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
      year = input("Enter Publishing Year: ").strip()
      if not validate_year(year):
        print("\nInvalid year. Please try again.")
        continue
      price = input("Enter Book Price: ").strip()
      if not validate_price(price):
        print("\nInvalid price. Please try again.")
        continue
      quantity = input("Enter Quantity: ").strip()
      if not validate_quantity(quantity):
        print("\nInvalid quantity. Please try again.")
        continue
      if library.add_book(title, author, int(year), float(price), int(quantity)):
        print("\nBook added successfully.")
      else:
        print("\nBook already exists, quantity updated.")

    elif choice == '2':
      print("\nView All Books")
      library.view_all_books()

    elif choice == '3':
      print("\nUpdate Book")
      isbn = input("Enter ISBN to update: ").strip()
      if not validate_isbn(isbn):
        print("\nInvalid ISBN. Please try again.")
        continue
      title = input("Enter new Title (or leave empty to skip): ")
      author = input("Enter new Author (or leave empty to skip): ")
      year = input("Enter new Year (or leave empty to skip): ").strip()
      price = input("Enter new Price (or leave empty to skip): ").strip()
      quantity = input("Enter new Quantity (or leave empty to skip): ").strip()
      year = int(year) if year and validate_year(year) else None
      price = float(price) if price and validate_price(price) else None
      quantity = int(quantity) if quantity and validate_quantity(quantity) else None
      library.update_book(int(isbn), title or None, author or None, year, price, quantity)

    elif choice == '4':
      print("\nRemove Book")
      isbn = input("Enter ISBN to remove: ").strip()
      if not validate_isbn(isbn):
        print("\nInvalid ISBN. Please try again.")
        continue
      library.remove_book(int(isbn))

    elif choice == '5':
      print("\nLend Book")
      isbn = input("Enter ISBN to lend: ").strip()
      if not validate_isbn(isbn):
        print("\nInvalid ISBN. Please try again.")
        continue
      borrower_name = input("Enter Borrower's Name: ")
      borrower_phone = input("Enter Borrower's Phone Number: ")
      due_date = input("Enter Due Date (YYYY-MM-DD): ").strip()
      if not validate_date(due_date):
        print("\nInvalid date format. Please try again.")
        continue
      library.lend_book(int(isbn), borrower_name, borrower_phone, due_date)

    elif choice == '6':
      print("\nReturn Book")
      isbn = input("Enter ISBN to return: ").strip()
      if not validate_isbn(isbn):
        print("\nInvalid ISBN. Please try again.")
        continue
      library.return_book(int(isbn))

    elif choice == '7':
      print("\nSaving and Exiting...")
      library.save()
      print("Books saved. Exiting...\n")
      break
    else:
      print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
  main()