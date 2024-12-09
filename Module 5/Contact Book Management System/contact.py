class Contact:
  def __init__(self, name, email, phone, address) -> None:
    self.name = name
    self.email = email
    self.phone = phone
    self.address = address
  
  def __str__(self) -> str:
    return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}"
  
  def matches(self, search_term):
    search_term = search_term.lower()
    return (search_term in self.name.lower() or
            search_term in self.email.lower() or
            search_term in self.address.lower())