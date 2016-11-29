#Display Table Data
import pymysql

# Open database connection
db =pymysql.connect(host='localhost',
    user='root',
    passwd='iamwithyou',
    db='mydb')
print("Database Connection Successful!!!")
cursor = db.cursor()

print("The Database Table contents are: ")
sql = "SELECT * FROM tblemp"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # Now print fetched result
      print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income ))
except:
   print ("Error: unable to fecth data")

# disconnect from server
db.close()
