import math
from math import sqrt

class ModulesDemo():

    def builtin_modules(self):
        print(math.sqrt(100))
        print(sqrt(100))

    def method1(self):
        print('this is module sample')

    def method2(self):
        print('this is a sample')


m = ModulesDemo()

m.method1()
m.method2()
m.builtin_modules()
