"""
Break: To break out of the closest enclosing loop
Continue: Go to the start of the closest enclosing loop
"""

x = 0
while x< 10:
    print("Value of x is: " + str(x))
    x=x+1

    if x ==8:
        break

    print("Done")

else:
    print("just broke out of the loop")