# Contact Book Management System

A Python-based Command-Line Interface (CLI) Contact Book Management System that allows users to manage their contacts efficiently. The system is built with Object-Oriented Programming (OOP) principles and ensures modularity by separating logic into independent and dependent components.

---

## Architecture Overview

### Independent Components:

- **Contact Class (`contact.py`)**  
  Defines the data structure for a contact, including attributes like name, phone, email, and address.

- **FileHandler Class (`file_handler.py`)**  
  Handles file operations for saving and loading contacts in CSV format.

- **Validation Functions (`validation.py`)**  
  Provides utility functions to validate contact details (e.g., name, phone number, and email).

### Dependent Components:

- **ContactManager Class (`contact_manager.py`)**  
  Manages contact operations, including adding, viewing, removing, and searching contacts.

### Entry Point:

- **Main Script (`main.py`)**  
  Serves as the user interface and the main entry point for interacting with the `ContactManager`.

---

## Data Flow Diagram (DFD)

The following diagram illustrates the flow of data between the components in the system:

graph TD
    %% Start of the program
    Start[Start] --> LoadContacts[Load Contacts from CSV]
    LoadContacts --> MainMenu[Display Main Menu]

    %% User Decision and Menu Options
    MainMenu --> UserChoice{User Choice}

    %% Option 1: Add Contact
    UserChoice -->|Option 1: Add Contact| RequestDetails[Request Name, Email, Phone, Address]
    RequestDetails --> ValidateName{Validate Name}
    ValidateName -->|Valid| ValidatePhone{Validate Phone}
    ValidateName -->|Invalid| InvalidName[Invalid Name Error]
    ValidatePhone -->|Valid| ValidateEmail{Validate Email}
    ValidatePhone -->|Invalid| InvalidPhone[Invalid Phone Error]
    ValidateEmail -->|Valid| AddContact[Add Contact]
    ValidateEmail -->|Invalid| InvalidEmail[Invalid Email Error]
    AddContact --> MainMenu

    %% Option 2: View Contacts
    UserChoice -->|Option 2: View Contacts| ShowContacts[Show All Contacts]
    ShowContacts --> MainMenu

    %% Option 3: Remove Contact
    UserChoice -->|Option 3: Remove Contact| RequestPhone[Request Phone Number]
    RequestPhone --> ContactExists{Contact Exists?}
    ContactExists -->|Yes| RemoveContact[Remove Contact]
    ContactExists -->|No| ContactNotFound[Contact Not Found Error]
    RemoveContact --> MainMenu

    %% Option 4: Search Contact
    UserChoice -->|Option 4: Search Contact| RequestSearch[Request Search Term]
    RequestSearch --> DisplaySearchResults[Display Search Results]
    DisplaySearchResults --> MainMenu

    %% Option 5: Exit Program
    UserChoice -->|Option 0: Exit| SaveContacts[Save Contacts to CSV]
    SaveContacts --> Exit[Exit]

    %% Node Styling for compact layout and readable format
    class Start,LoadContacts,MainMenu,SaveContacts,Exit fill:#000000,stroke:#f2f2f2,stroke-width:2px;
    class RequestDetails,AddContact,ShowContacts,RequestPhone,RemoveContact,RequestSearch,DisplaySearchResults fill:#000000,stroke:#f2f2f2,stroke-width:2px;
    class InvalidName,InvalidPhone,InvalidEmail,ContactNotFound fill:#5c5c5c,stroke:#f2f2f2,stroke-width:2px;
    class UserChoice,ValidateName,ValidatePhone,ValidateEmail,ContactExists fill:#333333,stroke:#f2f2f2,stroke-width:2px;

    %% Adjusting the compact layout and distances between nodes
    InvalidName -->|Retry| ValidatePhone
    InvalidPhone -->|Retry| ValidateEmail
    InvalidEmail -->|Retry| AddContact
    ContactNotFound -->|Retry| RemoveContact