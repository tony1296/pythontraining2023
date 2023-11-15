#write the data to atext file

obj=open("C:\\Users\\HP\\PycharmProjects\\pythontraining2023\\File Handling\\write1.txt", 'w')
obj.write("This is manual testing")
obj.close()

#append the data to file

obj=open("C:\\Users\\HP\\PycharmProjects\\pythontraining2023\\File Handling\\write1.txt", 'a')
obj.write("This is automation testing")
obj.close()