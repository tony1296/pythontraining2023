class Student:
    # constructor - non paramaterized
    def __init__(self):
        print('this is non parametrized constructor')
    def show(self,name):
        print('hello',name)
st= Student()
st.show('sree')