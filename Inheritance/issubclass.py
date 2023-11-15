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
print(issubclass(Derived,Caluclation2))
print(issubclass(Caluclation1,Caluclation2))
print(issubclass(Derived,Caluclation1))