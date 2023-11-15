try:
    x=str
    y=50
    print(y)
    print(x)

except NameError:
    print("Variable x is not defined")
except TypeError:
    print("Variable y is not defined:" +str(y))
finally:
    print("finally executed")