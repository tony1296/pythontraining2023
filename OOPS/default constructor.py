"""
constructor is a method having the same name as the class name.
The main purpose of constructor is to initialize the data.

types of constructors
1.default constructor
2.parameter constructor
"""

class Student:
    roll_num = 316
    name = 'srikanth'

    def display(self):
        print(self.roll_num, self.name)

st = Student()
st.display()