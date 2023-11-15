"""
1. not
2. and
3. or
"""

bool_output = True or not False and False
# True
print(bool_output)

bool_output_1 = (15 == 15 or not 15 >15) and 15 > 15
# True or True -> True and False -> False
print(bool_output_1)