import openpyxl

wb=openpyxl.Workbook()
sh=wb.active
sh.title="Testing"
print(sh.title)
sh['A5'].value="Manual"
#create second sheet
wb.create_sheet(title="Python")
sh1=wb['Python']
sh1['B3'] =("8066")
#remove sheet
wb.remove(wb['Python'])
wb.save("C:\\Users\\HP\\Desktop\\writeexcel.xlsx")