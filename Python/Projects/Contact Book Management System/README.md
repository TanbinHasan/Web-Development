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

![Flowchart](https://raw.githubusercontent.com/TanbinHasan/Web-Development/master/Module%205/assets/CBMS.png)
