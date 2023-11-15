"""
Variable Scope
"""
a = 120

def test_method(a):
    print("Value of local 'a' is:" + str(a))
    a=4
    print("New value of local 'a' is: "+ str(a))

print("Value of global 'a' is:" + str(a))
test_method(a)
print("Did the value of global 'a' change?" + str(a))

a=75

def test_method():
    global a,b
    print("Value of 'a' inside the method is:" + str(a))
    a=8
    print("New value of 'a' inside the method is changed to:" + str(a))
    b=5
    print("new value of b:" + str(b))

print("Value of global a is :" + str(a))
test_method()
print("Did the value of global 'a' change?" + str(a))