class Caluclation1:

    def Summation(self,a,b):
        return a+b;

class Caluclation2:

    def Multiplication(self,a,b):
        return a*b;

class Derived(Caluclation1,Caluclation2):

    def Divide(self,a,b):
        return a/b;

d = Derived()
print(d.Summation(10,15))
print(d.Multiplication(10,15))
print(d.Divide(10,15))