import openpyxl
ptr=openpyxl.load_workbook('sheet1.xlsx')
excltype=type(ptr)
print("The Excel Datatype is: ",excltype)
print("The Sheets in the workbook are: ",ptr.get_sheet_names())
print("Enter the sheet name to open:\t")
sheetnm=input()
sheet=ptr.get_sheet_by_name(sheetnm)
print("The title of the sheet is: ",sheet.title)
print("Opening the first sheet of the excel file....")
currsheet=ptr.active
print("The current sheet title is: ",currsheet.title)
