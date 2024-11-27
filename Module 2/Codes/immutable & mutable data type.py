# immutable data type: Memory address changes after modification
# i.e: int, float, string, tuple, frozen set
# mutable data type: Memory address doesn't change after modification

a = 5
print(id(a)) # print the memory address ot the variable
a = 6
print(id(a))

b = {1, 2, 3}
print(id(b))

b.add(5)
print(id(b))
print(b)