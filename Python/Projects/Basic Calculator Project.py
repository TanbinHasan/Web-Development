print("Welcome to Calculator Project")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

option = int(input("Select an option for Basic Calculator Operation: "))

x = int(input("Enter the 1st number: "))
y = int(input("Enter the 2nd number: "))

if option == 1: print("Addition is: %d\n" %(x + y))
elif option == 2: print("Subtraction is: %d\n" %(x - y))
elif option == 3: print("Multiplication is: %d\n" %(x * y))
elif option == 4:
  if y == 0: print("Error: Division by zero is not allowed.\n")
  else: print("Division is: %.9f\n" %(x / y))
else: print("Invalid Input")