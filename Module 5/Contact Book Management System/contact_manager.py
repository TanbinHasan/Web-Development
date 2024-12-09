from contact import Contact
from file_handler import FileHandler

class ContactManager:
  def __init__(self) -> None:
    self.contacts = {}
    self.file_handler = FileHandler("contacts.csv")

  def load_contacts(self):
    self.contacts = self.file_handler.load()

  def save_contacts(self):
    self.file_handler.save(self.contacts)
  
  def add_contact(self, name, email, phone, address):
    if phone in self.contacts:
      return False
    self.contacts[phone] = Contact(name, email, phone, address)
    return True
  
  def view_contacts(self):
    if not self.contacts:
      print("No contacts available.")
      return
    print("\n--- Contact List ---")
    for contact in self.contacts.values():
      print(contact)
    print()
  
  def remove_contact(self, phone):
    if phone in self.contacts:
      del self.contacts[phone]
      return True
    return False
  
  def search_contacts(self, search_term):
    return [contact for contact in self.contacts.values() if contact.matches(search_term)]