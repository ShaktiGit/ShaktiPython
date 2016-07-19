import csv
file1=open("csvfile.csv")
file1reader=csv.reader(file1)
csvlist=list(file1reader)
print("The CSV file contents are: ",csvlist)
