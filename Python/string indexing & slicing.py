s = "Tanbin Hasan Ador"

# positive indexing
print(s[2]) # 3rd character
# negative indexing
print(s[-1]) # last character
print(s[-2]) # second last character


# string slicing
print(s[0 : 6]) # print 0 to 5th character
print(s[7: ]) # from 7th character to the end
print(s[ : 10]) # from begin to 9th character

print(s[::2]) # extracts every 2nd character
print(s[::-1]) # reverse the string
print(s[0::3]) #extract every third character from index 0