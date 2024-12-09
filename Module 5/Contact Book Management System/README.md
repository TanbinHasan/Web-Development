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

![Diagram](https://mermaid.ink/img/pako:eNqdVm1P2zAQ_iuWEd8MavpOJm1ClEmTRjdRhrS1fDCJSzMSu7MdoGv73-e3JHYpgy2Vqtz5uRffPT5nDROWEhjDO46XC3A1mlGgnsNDMJGYS8DmQC4IWHKmAIVdNCtT838Djo7eg88Mp2eMSpxIMdUCqCQw56wAZ5PrG2vqI43pBc7oBaHldJSJZY5XRgG0RlnUuXwThIMRSTKRMQowTQ0CfFlKJQsLqzwZt9rgbMGyhKyNrX3fei6tLYhicJrW-drVxlj72uxFbsAl-VUSIUdE4iwXUyeCMS4IAueFUiLwdcGokpQdJ0K4GoSGJt1rnGcplkQbryvBuNpaGx9gkjKKTa03gRpLI75k-ok-WGP3ohem7t3EBOecM34TmhuX-0KbrTahjbh9yXY3tlmpg1vcvujGqx9dldR1Yup15UWr3bhmpY5rcX7cxn3A0uf8acfgOiOPNeH_xqBd7AZMFuyxPjhaAKd5Xq-7XHzQK9l0YsWugj2QtxD6GbjmtO1KxWjblXFZ3BIeUrjua-Xh_CkTUqyr0lnxg2NDgDGJfCdi43KomhlmdPOS5ZhtKu2YyY-spOm0iqoUwGiCjgZhXiljNwYTgnmyeEsZn4HrMlp1XUeHuiK8CMvoFnRObgpazSURZa6IUY1Gh3Nq52OfxSvb68W6M6qx_lDfv7mWhSqm4rp4iqm4aZEAknkD3seZNLT5VP_583ys7hx1jazyjN6BOeMgYcVS90XthJXSTHhOcIpvc6LXC-xakORYCHsBIf8uQdVukZ8AMtucZ3keH7TMg4Tk7J7EB_O2_jnx6DFL5SJuL5_e-WHCQY2amYD8I4n8w4ACmqGgwWhvq_47O296I3-aIn_EoZ1D4sL1Ev37p3ANP5B_o6BgxqNg8qLw3NrQHfO8IXRNltP0ZymkZor-EtnDlFS5xzQhAtwS-UgIBVTxy
