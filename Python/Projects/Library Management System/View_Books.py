from LibraryData import all_books

# View all books
def view_all_books():
  if all_books:
    for book in all_books:
      print(f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']}")
  else: print("There are no books.")
