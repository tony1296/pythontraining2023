"""
Dictionary Methods
"""

car = {'make':'bmw','model':'550q','year': 2015}
cars = {'bmw': {'model': '550q','year': 2018},'benz':{'model':'e350','year':2018}}

print(car.keys())

print(cars.keys())
print(car.values())
print(cars.values())
print(car.items())
print(cars.items())
car_copy = car.copy()
print(car_copy)

print(car.pop('model'))
print(car)