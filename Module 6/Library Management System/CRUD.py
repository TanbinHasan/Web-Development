# Create, Read, Update, Delete -> CRUD
import csv

from LibraryData import all_books

# Load books from the CSV file at the start
def load_books():
  try:
    with open("all_books.csv", "r") as fp:
      reader = csv.DictReader(fp)
      for row in reader:
        all_books.append({
          "title": row["title"],
          "author": row["author"],
          "isbn": int(row["isbn"]),
          "year": int(row["year"]),
          "price": int(row["price"]),
          "quantity": int(row["quantity"]),
        })
  except FileNotFoundError: print("No existing book data found. Starting with an empty library.")

# Save books to the CSV file
def save():
  with open("all_books.csv", "w", newline="", encoding="utf-8") as fp:
    fieldnames = ["title", "author", "isbn", "year", "price", "quantity"]
    writer = csv.DictWriter(fp, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_books)

# Add a book
def add():
  title = input("Enter Book Title: ")
  author = input("Enter Author Name: ")
  isbn = int(input("Enter ISBN Number: "))
  year = int(input("Enter Publishing Year Number: "))
  price = int(input("Enter Book Price: "))
  quantity = int(input("Enter Quantity Number: "))

  book = {
    "title": title,
    "author": author,
    "isbn": isbn,
    "year": year,
    "price": price,
    "quantity": quantity,
  }

  all_books.append(book)
  save()
  print("Book Added Successfully")

# Remove a book by ISBN
def remove():
  isbn = int(input("Enter ISBN Number of the book to remove: "))
  for book in all_books:
    if book["isbn"] == isbn:
      all_books.remove(book)
      save()
      print("Book Removed Successfully")
      return
  print("No book found with the given ISBN")

# Update a book's details by ISBN
def update():
  isbn = int(input("Enter ISBN Number of the book to update: "))
  for book in all_books:
    if book["isbn"] == isbn:
      print("Book found. Enter new details (leave blank to keep current value):")
      book["title"] = input(f"Title ({book['title']}): ") or book["title"]
      book["author"] = input(f"Author ({book['author']}): ") or book["author"]
      book["year"] = int(input(f"Year ({book['year']}): ") or book["year"])
      book["price"] = int(input(f"Price ({book['price']}): ") or book["price"])
      book["quantity"] = int(input(f"Quantity ({book['quantity']}): ") or book["quantity"])
      save()
      print("Book Updated Successfully")
      return
  print("No book found with the given ISBN")