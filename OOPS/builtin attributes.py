'''
__dict__ It provides the dictionary containing the information about the class namespace
_doc__ It contains a string which has the class documentation
__module__ It is used to access the module in which, this class is defined
'''

class Student:

    def __init__(self,name,id,age):
        self.name = name;
        self.id = id;
        self.age = age
    def display_details(self):
        print("Name:%s, ID:%d, age:%d"%(self.name,self.id,self.age))
s = Student("srikanth",8066,316)
s.display_details()
print(s.__doc__)
print(s.__dict__)
print(s.__module__)