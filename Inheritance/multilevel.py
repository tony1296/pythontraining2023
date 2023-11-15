class sample1:

    def print1(self):
        print("this is sample1")

class sample2(sample1):

    def print2(self):
        print("this is sample2")

class sample3(sample2):

    def print3(self):
        print("this is sample3")




s = sample3()

s.print1()
s.print2()
s.print3()
