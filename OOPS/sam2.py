class Employee:



    def __init__(self,name,id):

        self.id = id
        self.name = name


    def display(self):
        print("ID: %d \nName: %s" % (self.id,self.name))

e1 = Employee('sree', 10)
e2 = Employee('hari', 20)
e3 = Employee('sai',45)

# accessing display() method to print employee 1,2,3 information

e1.display()
e2.display()
e3.display()