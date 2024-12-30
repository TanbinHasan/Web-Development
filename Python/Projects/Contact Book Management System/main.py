from contact_manager import ContactManager
from validation import validate_name, validate_phone, validate_email

def main():
  manager = ContactManager()
  manager.load_contacts()

  while True:
    print("---My Contact Book---")
    print("0. Exit")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Remove Contact")
    print("4. Search Contact")
    
    choice = input("\nChoose an option: ")

    if choice == '0':
      manager.save_contacts()
      print("\nExiting. Contacts saved.\n")
      break
    
    if choice == '1':
      name = input("\nEnter Name: ")
      email = input("Enter Email: ")
      phone = input("Enter Phone Number: ")
      address = input("Enter Address: ")

      if validate_name(name) and validate_phone(phone) and validate_email(email):
        if manager.add_contact(name, email, phone, address):
          print("\nContact added successfully.\n")
        else:
          print("\nPhone number already exists.\n")
      else:
        print("\nInvalid input. Try again.\n")

    elif choice == '2':
      manager.view_contacts()

    elif choice == '3':
      phone = input("\nEnter Phone Number of the Contact to Remove: ")
      if manager.remove_contact(phone):
        print("\nContact removed successfully.\n")
      else:
        print("\nContact not found.\n")
    
    elif choice == '4':
      search_term = input("\nEnter Name, Email or Address to search: ")
      result = manager.search_contacts(search_term)
      if result:
        print("\nSearch Results:")
        for contact in result:
          print(contact)
      else:
        print("\nNo matching contacts found.\n")
    
    else:
      print("\nInvalid option. Please try again.\n")

if __name__ == "__main__":
  main()