import csv
from contact import Contact

class FileHandler:
  def __init__(self, file_path) -> None:
    self.file_path = file_path
  
  def load(self):
    contacts = {}
    try:
      with open(self.file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
          contacts[row['Phone']] = Contact(
            name=row['Name'],
            email=row['Email'],
            phone=row['Phone'],
            address=row['Address']
          )
    except FileNotFoundError:
      pass
    return contacts
  
  def save(self, contacts):
    with open(self.file_path, mode='w', newline='') as file:
      fieldnames = ['Name', 'Email', 'Phone', 'Address']
      writer = csv.DictWriter(file, fieldnames=fieldnames)
      writer.writeheader()
      for contact in contacts.values():
        writer.writerow({
          'Name': contact.name,
          'Email': contact.email,
          'Phone': contact.phone,
          'Address': contact.address
        })