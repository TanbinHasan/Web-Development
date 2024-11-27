# range data type
num = range(1, 10) # store 1 to 9
print(num) # print the range
print(*num) # print all the number in the range
print(type(num)) # check data types
num2 = range(1, 20, 3) # store 1 to 19 in this way 1, 4, 7...
print(*num2)
num3 = range(7) # 0 to 6
print(*num3)

# None Data Type
taka = None
print(type(taka))

# Dictionary Data Type
person = {
  'first_name': 'John',
  'last_name': 'Cena',
  'age': 23
}
print(person)
print(person['first_name'])