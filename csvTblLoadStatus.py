#Load csv/flat file contents into database
#http://stackoverflow.com/questions/10154633/load-csv-data-into-mysql-in-python
import csv
import pymysql
import random
import time
import datetime
import socket,os
from stat import *

# Open database connection
db =pymysql.connect(host='localhost',
    user='root',
    passwd='iamwithyou',
    db='mydb')
print("Database Connection Successful!!!")
cursor = db.cursor()
filenm='F:\\tech mahindra\\ALL\\python\\pycsvfiles\\student.csv'
# Counting file size
st = os.stat('F:\\tech mahindra\\ALL\\python\\pycsvfiles\\student.csv')
fsize=str(st[ST_SIZE])
print("File Size: ",fsize)
dest='mydb\\tblcsv'
ipaddr=socket.gethostbyname(socket.gethostname())
print("IP Address: ",ipaddr)
filereader=open(filenm,"r")
print("The file opened!!")
print("The CSV input file contents are: ")
recno=0
randval=0
loadstatus="RED"
lidloadsts=""
csv_data = csv.reader(filereader)
try:
    lidloadsts="NOT LOADED"
    for row in csv_data:
        recno=recno+1
        lidroll=row[1]
        randval=random.randint(1,999999)
        ts = time.time()
        lidtime = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        print("LID: ",randval)
        print("CSV Record:")
        print(row)
        cursor.execute('INSERT INTO tblcsv(name,roll) VALUES("%s", "%s")',row)
        print("1 Record Inserted!!!")
        lidloadsts="LOADED"
        #LID insertion into tblcsvlid
        print("randval:",randval)
        print("lidroll:",lidroll)
        print("lidtime:",lidtime)
        slidtime=str(lidtime)
        print("filenm:",filenm)
        print("dest:",dest)
        print("ipaddr:",ipaddr)
        print("fsize:",fsize)
        print("lidloadsts:",lidloadsts)
        cursor.execute('INSERT INTO tblcsvlid(lid,roll,lidtime,source,dest,ipaddr,fsize,loadsts) VALUES("%s", "%s","%s","%s","%s","%s","%s","%s")',(randval,lidroll,slidtime,filenm,dest,ipaddr,fsize,lidloadsts))
        print("Random no inserted into tblcsvlid")
        db.commit()
               
    print("Database Loading completed!!!")
    
          
except:
    db.rollback()
    print("CSV Loading Failed !!")
#close the connection to the database.
cursor.close()
# Report Generation for DB load
print("Total No Of Records Inserted: ",recno)
print("*****************************************")
print("The Database Table contents are: ")
fetchcursor = db.cursor()
sql = "SELECT * FROM tblcsv"
rescount=0
try:
   # Execute the SQL command
   fetchcursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = fetchcursor.fetchall()
   for row in results:
       rescount=rescount+1
       sname = row[0]
       sroll = row[1]
       # Now print fetched result
       print ("Student Name=%s,Student Roll=%s" % \
             (sname, sroll ))
except:
   print ("Error: unable to fecth data")

# disconnect from server
fetchcursor.close()
db.close()
print("*****************************************")
if rescount==recno:
    loadstatus="GREEN"
    val=1
    per=val * 100
    print("Table Loading Percent: ",per," %")
    print("Table Loading Status: ",loadstatus)
elif rescount<recno:
    loadstatus="RED"
    val=(recno-rescount)/recno
    per=val * 100
    print("Table Loading Percent: ",per," %")
    print("Table Loading Status: ",loadstatus)
else:
    print("Table already contains data before csv load !!")
    
    
