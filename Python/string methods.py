s = "james-hetfield"

print(s.upper()) # convert to uppercase
print(s.lower()) # convert to lowercase
print(s.capitalize()) #capitalize the first letter
print(s.title()) # capitalize the first letter of each word
print(s.swapcase()) # invert case of each letter

print(s.replace('hetfield', 'faulkner'))

words = s.split("-")
print(words)
for i in range(len(words)):
  print(words[i], end=" " if i != len(words) - 1 else "\n")
print("Ador")