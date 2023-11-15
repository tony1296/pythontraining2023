"""
logical operators
and
*************************
True and True ---> True
True and False ---> False
False and False ---> False
****************************

or
*************************
True or True ---> True
True or Flase ---> True
False or False ---> False
*************************

not
****************************
Not True --> False
Not False --> True
"""


and_output1 = (20 == 20) and (20 > 19)
and_output2 = (20 == 20) and (20 < 19)
and_output3 = (20 > 20) and (20 < 19)

or_output1 = (20 == 20) or (20 > 19)
or_output2 = (20 == 20) or (20 < 19)
or_output3 = (20 > 20) or (20 < 19)

not_true = not (20 == 20)
not_true = not (20 > 22)
not_false = not (20 > 20)

print(and_output1)
print(and_output2)
print(and_output3)
print(or_output1)
print(or_output2)
print(or_output3)
print(not_true)
print(not_true)
print(not_false)
