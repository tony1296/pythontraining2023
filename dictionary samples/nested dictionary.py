"""
Nested dictionary
d = {'k1 : {'nestk1':'nestvalue1','nestk2':'nestvalue2'}}
d['k1']['nestk1']
"""

cars = {'bmw':{'model': '330q', 'year': 2014},'benz': {'model':'e500','year': 2017}}
bmw_year = cars['bmw']['year']
print(bmw_year)
print(cars['benz']['model'])