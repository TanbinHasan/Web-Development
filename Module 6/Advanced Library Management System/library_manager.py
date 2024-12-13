from random import randint
from book import Book
from file_handler import FileHandler
from datetime import datetime

class LibraryManager:
  def __init__(self, file_path):
    self.file_handler = FileHandler(file_path)
    self.books, self.lent_books = self.file_handler.load()
    self.existing_isbn = set(book.isbn for book in self.books.values())

  def add_book(self, title, author, year, price, quantity):
    for book in self.books.values():
      if (book.title == title and book.author == author and book.year == year and book.price == price):
        book.quantity += quantity
        return False
    new_book = Book(title, author, year, price, quantity)
    while new_book.isbn in self.existing_isbn:
      new_book.isbn = randint(100000, 10000000)
    self.books[str(new_book.isbn)] = new_book
    self.existing_isbn.add(new_book.isbn)
    return True

  def view_all_books(self):
    if not self.books:
      print("No books available.")
      return
    for book in self.books.values():
      print(book)

  def update_book(self, isbn, title=None, author=None, year=None, price=None, quantity=None):
    book = self.books.get(str(isbn))
    if not book:
      print(f"Book with ISBN {isbn} not found.")
      return
    if title: book.title = title
    if author: book.author = author
    if year: book.year = year
    if price: book.price = price
    if quantity is not None: book.quantity += quantity
    print(f"Book {isbn} updated successfully.")

  def remove_book(self, isbn):
    if str(isbn) in self.books:
      del self.books[str(isbn)]
      print(f"Book {isbn} removed successfully.")
    else:
      print(f"Book with ISBN {isbn} not found.")

  def lend_book(self, isbn, borrower_name, borrower_phone, due_date):
    isbn_str = str(isbn)
    book = self.books.get(isbn_str)
    if book and book.quantity > 0:
      book.quantity -= 1
      book.bookLastUpdatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      self.lent_books[isbn_str] = {
        'borrower_name': borrower_name,
        'borrower_phone': borrower_phone,
        'due_date': due_date
      }
      print(f"Book {isbn_str} lent to {borrower_name}. Due date: {due_date}.")
    else:
      print("There are not enough books available to lend.")

  def return_book(self, isbn):
    isbn_str = str(isbn)
    book = self.books.get(isbn_str)
    if isbn_str in self.lent_books:
      book.quantity += 1
      del self.lent_books[isbn_str]
      book.bookLastUpdatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      print(f"Book {isbn_str} returned successfully.")
    else:
      print(f"Book with ISBN {isbn_str} was not lent out.")

  def save(self):
    self.file_handler.save(self.books, self.lent_books)