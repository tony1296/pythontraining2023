class student:
    count = 0

    def __init__(self):
        student.count = student.count + 1

s1=student()
s2=student()
s3=student()
print('the number of students:', student.count)