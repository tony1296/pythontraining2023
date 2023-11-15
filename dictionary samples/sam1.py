"""
Data type to store more than one value in one variable name, in terms of key value pairs
Dictionary items are in brackets {} in key:value pairs, separated with ","{'k1:'v1','k2:v2}
Not sequenced , no indexing -> Mapping
"""

car = {"make": 'hyndai','model': '220e', 'year': 2017}
print(car)

model = car['model']
print(car['make'])
print(model)

d = {}

d['one'] = 1
d['two'] = 2

print(d)

sum_1 = d['two'] + 9
print(sum_1)
print(d)
d['two'] = d['two'] + 9
print(d)