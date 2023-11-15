import csv

f=open("C:\\Users\\HP\\Desktop\\csvwrite.csv",'w',newline='')
csv_v=csv.writer(f)
csv_v.writerow(['hi',1,22])
csv_v.writerow(['if',2,308])
csv_v.writerow(['hee',12,203])
f.close()