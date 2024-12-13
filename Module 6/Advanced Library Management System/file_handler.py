import json
from book import Book

class FileHandler:
  def __init__(self, file_path):
    self.file_path = file_path

  def load(self):
    try:
      with open(self.file_path, 'r') as file:
        data = json.load(file)
        
        # Handle case when data is a list instead of a dictionary
        if isinstance(data, list):
          data = {"books": data, "lent_books": {}}
        
        book_dict = {}
        lent_books = data.get("lent_books", {})

        for book in data.get("books", []):
          book_dict[str(book['isbn'])] = Book(**book)
        
        return book_dict, lent_books
    except FileNotFoundError:
      return {}, {}

  def save(self, books, lent_books):
    with open(self.file_path, 'w') as file:
      data = {
        "books": [book.__dict__ for book in books.values()],
        "lent_books": lent_books
      }
      json.dump(data, file, indent=2)
