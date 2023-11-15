'''
Inheritance is the process of creating a new class from an existing class
The existing class we call it as base class or parent class or super class
and the newly created class we call it as derived class or sub class or child class

Types of inheritance supported in python are

single
multiple
multilevel
hierarchical
hybrid
'''
#single inheritance

class sample1:

    def display(self):
        print("this is sample example")

    def display1(self):
        print("this is a sample")

class sample2(sample1):

    def print(self):
        print("this is sample2 example")

    def print1(self):
        print("this is a sample")

s = sample2()
s.display()
s.display1()
s.print()