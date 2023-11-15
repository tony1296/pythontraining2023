"""
examples to show available string methods in python
"""

# accessing characters in a string
# index starts from zero
place = "my home"
city = "hyderabad"
print(place[3])
gt = city[3]
print(gt)
print(city[3])

"""
string methods
len()
lower()
upper()
str()
"""
stri = "Srikanth"
print(stri.lower())
print(stri.upper())
print(stri+"3")
print(len(stri))
#or
print(stri + str(3))

"""
concatenation
"""
print("Hello" + "  " + "World !!")
print(place + city)
print(place + "   " + city)
print('good morning')