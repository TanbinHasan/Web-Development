def validate_name(name):
  return name.isalpha()

def validate_phone(phone):
  return phone.isdigit() and len(phone) in [11, 14]

def validate_email(email):
  return "@" in email and "." in email