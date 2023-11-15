"""""
Built in methods to help manipulating a list
"""""

cars = ["bmw","honda","audi"]

length = len(cars)
print(length)
print("*"*10)
cars.append("benz")
print(cars)
print("*"*10)
cars.insert(1,"jeep")
print(cars)
print("*"*10)
x = cars.index("honda")
print(x)
print("*"*10)
y = cars.pop()
print(y)
print(cars)
print("*"*10)
cars.remove("jeep")
print(cars)
print("*"*10)
slicing = cars[0:2]
a = cars[1:]
print(slicing)
print(a)
print("*"*10)
print(cars)