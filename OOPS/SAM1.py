class Employee:
    id = 20
    name = 'srikanth'


    def display(self):

        print("ID: %d \nName: %s" % (self.id, self.name))


e = Employee()
e.display()