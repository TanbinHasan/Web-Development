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

```mermaid
graph TD
  A[User] -->|Interacts with| B[Main Script (main.py)]
  B -->|Calls| C[ContactManager (contact_manager.py)]
  C -->|Uses| D[Validation Functions (validation.py)]
  C -->|Uses| E[FileHandler (file_handler.py)]
  E -->|Reads/Writes| F[CSV File]
  C -->|Manages| G[Contact Objects (contact.py)]

  subgraph MainScript [Main Script (main.py)]
    direction TB
    B0[Load Contacts]
    B1[Add Contact]
    B2[View Contacts]
    B3[Remove Contact]
    B4[Search Contact]
    B5[Save Contacts]
    B --> B0
    B --> B1
    B --> B2
    B --> B3
    B --> B4
    B --> B5
  end

  subgraph ContactManager [ContactManager (contact_manager.py)]
    direction TB
    C0[Validate Input]
    C1[Add Contact]
    C2[View Contacts]
    C3[Remove Contact]
    C4[Search Contact]
    C --> C0
    C --> C1
    C --> C2
    C --> C3
    C --> C4
    C0 --> D
    C1 --> G
    C2 --> G
    C3 --> G
    C4 --> G
    C1 --> E
    C2 --> E
    C3 --> E
    C4 --> E
  end

  subgraph Validation [Validation Functions (validation.py)]
    direction TB
    D0[validate_name(name)]
    D1[validate_phone(phone)]
    D2[validate_email(email)]
    D --> D0
    D --> D1
    D --> D2
  end

  subgraph FileHandler [FileHandler (file_handler.py)]
    direction TB
    E0[load()]
    E1[save(contacts)]
    E --> E0
    E --> E1
  end

  subgraph ContactObjects [Contact Objects (contact.py)]
    direction TB
    G0[Contact(name, email, phone, address)]
    G1[__str__()]
    G2[matches(search_term)]
    G --> G0
    G --> G1
    G --> G2
  end