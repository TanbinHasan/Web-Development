import random
from datetime import datetime

class Book:
  def __init__(self, title, author, year, price, quantity, isbn=None, bookAddedAt=None, bookLastUpdatedAt=None):
    self.title = title
    self.author = author
    self.year = year
    self.price = price
    self.quantity = quantity
    self.isbn = isbn or random.randint(100000, 10000000)
    self.bookAddedAt = bookAddedAt or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    self.bookLastUpdatedAt = bookLastUpdatedAt or ""

  def __str__(self):
    return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Year: {self.year}, Price: {self.price}, Quantity: {self.quantity}, Added At: {self.bookAddedAt}, Last Updated: {self.bookLastUpdatedAt}"

  def matches(self, search_term):
    search_term = search_term.lower()
    return (search_term in self.title.lower() or
      search_term in self.author.lower() or
      search_term in str(self.isbn))