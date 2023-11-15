"""
Example to show how string formatting works in python
"""

city = "Hyderabad"
event = "weather"

print("Welcome to " + city + " and enjoy the " + event)
print("welcome to"+city+"and enjoy the"+event)
print("welcome to %s" % city)
print("welcome to %s and enjoy the %s" %(city,event))