"""
Positional Parameters
They are like optional parameters
And can be assigned a default value, if no value is provided from outside
"""

global n2
def sum_num(n1,n2):
    """
    Get sum two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2

sum=sum_num(7,8)
print(sum)
sum1 = sum_num(5,n2=25)
print(sum1)
sum1=sum_num(n1=45,n2=74)
print(sum1)
