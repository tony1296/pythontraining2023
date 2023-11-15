class Student:
    def __init__(self):
        print('the first constructor')

    def __init__(self):
        print('the second constructor')

st = Student()

"""
the object st called the second constructor where as both have the same configuration
The first method is not accessible by the st object
Internally the object of the class will always call the last constructor if the class has multiple constructrs
Note: The constructor overloading is not allowed in python
"""
