def gen_by_terms(n):
  if n <= 0: return []
  v = []
  if n >= 1: v.append(0)
  if n >= 2: v.append(1)
  for i in range(2, n):
    v.append(v[i - 1] + v[i - 2])
  return v

def gen_by_value(n):
  if n < 0: return []
  v = []
  if n >= 0: v.append(0)
  if n >= 1: v.append(1)
  i = 2
  while True:
    nxt = v[i - 1] + v[i - 2]
    if nxt > n: break
    v.append(nxt)
    i += 1
  return v

def main():
  while True:
    print("\nChoose an option:")
    print("1. Generate Fibonacci series by number of terms")
    print("2. Generate Fibonacci series by maximum value")
    print("3. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
      try:
        n = int(input("Enter the number of terms: ").strip())
        if n < 0:
          print("Number of terms must be a non-negative integer.")
        else:
          v = gen_by_terms(n)
          print("Fibonacci series (%d terms):" % n, end=" ")
          for i in range(n):
            print(v[i], end=", " if i != n - 1 else "")
          print()
      except ValueError:
        print("Invalid input. Please enter a valid integer.")
    
    elif choice == "2":
      try:
        n = int(input("Enter the maximum value: ").strip())
        if n < 0:
          print("Value must be a non-negative integer.")
        else:
          v = gen_by_value(n)
          print("Fibonacci series (up to %d):" % n, end=" ")
          for i in range(len(v)):
            print(v[i], end=", " if i != len(v) - 1 else "")
          print()
      except ValueError:
        print("Invalid input. Please enter a valid integer.")
    
    elif choice == "3":
      print("Exiting the program. Goodbye!")
      break
    
    else:
      print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
  main()