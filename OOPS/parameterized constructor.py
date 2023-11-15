class Student:
    # constructor - parameterized
    def __init__(self, name):
        print('this is parameterized constructor')
        self.name = name
    def show(self):
        print('hello',self.name)
st = Student('sree')
st.show()