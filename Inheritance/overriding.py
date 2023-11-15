class Bank:
    def getroi(self):
        return 10;

    def print(self):
        print("this is sample")
class SBI(Bank):
    def getroi(self):
        return 8.5;

class ICICI(Bank):
    def getroi(self):
        return 7;

b1 = Bank()
b2 = SBI()
b3 = ICICI()
print("Bank ROI:",b1.getroi());
print("Bank ROI:",b2.getroi());
print("SBI ROI:", b2.getroi());
print("ICICI ROI:",b3.getroi());
