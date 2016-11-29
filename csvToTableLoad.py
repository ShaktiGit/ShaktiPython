#Load csv/flat file contents into database
#http://stackoverflow.com/questions/10154633/load-csv-data-into-mysql-in-python
import csv
import pymysql

# Open database connection
db =pymysql.connect(host='localhost',
    user='root',
    passwd='iamwithyou',
    db='mydb')
print("Database Connection Successful!!!")
cursor = db.cursor()
filereader=open('F:\\tech mahindra\\ALL\\python\\pycsvfiles\\student.csv',"r")
print("The file opened!!")
print("The CSV input file contents are: ")
csv_data = csv.reader(filereader)
try:
    
    for row in csv_data:
        print(row)
        cursor.execute('INSERT INTO tblcsv(name,roll) VALUES("%s", "%s")',row)
        print("1 Record Inserted!!!")
        db.commit()
    print("Database Loading completed!!!")
    
          
except:
    db.rollback()
    print("CSV Loading Failed !!")
#close the connection to the database.
cursor.close()
