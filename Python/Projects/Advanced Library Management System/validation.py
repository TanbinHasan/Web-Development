import re

def validate_name(name):
  return bool(name) and all(x.isalnum() or x.isspace() for x in name)

def validate_phone(phone):
  return phone.isdigit() and len(phone) in [11, 14]

def validate_email(email):
  return "@" in email and "." in email

def validate_year(year):
  return year.isdigit() and len(year) == 4 and int(year) <= 2024

def validate_date(date_str):
  """Validates if the date is in YYYY-MM-DD format."""
  pattern = r"^\d{4}-\d{2}-\d{2}$"
  return bool(re.match(pattern, date_str))

def validate_price(price):
  return price.isdigit() and int(price) > 0

def validate_quantity(quantity):
  return quantity.isdigit() and int(quantity) > 0

def validate_isbn(isbn):
  return isbn.isdigit() and 100000 <= int(isbn) <= 10000000