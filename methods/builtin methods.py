"""
Some built-in functions
max(): It takes any number of arguments and returns the largest one.

min(): It takes any number of arguments and returns the smallest one.

abs(): It returns the absolute value of the number,that number's distance from 0.
It always returns a positive value and it only takes a single number.

type():  It returns the type of the data it recieves as an argument

"""

def largest_num(*args):
    print(max(args))

    #return(max(args))
largest_num(-10,-18,0,12,23,25)

def smallest_num(*args):
    print(min(args))

smallest_num(-48,-25,-4,0,14,85,96)

def abs_function(a):
    print(abs(a))
abs_function(-14.5)
abs_function(12.5)
print("***********")

print(type(99))
print(type(99.9))
print(type("99.9"))
l = [1,2,3]
print(type(l))