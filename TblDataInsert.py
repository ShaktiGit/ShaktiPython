#Inserting data into the table
#https://www.tutorialspoint.com/python3/python_database_access.htm
import pymysql

# Open database connection
db =pymysql.connect(host='localhost',
    user='root',
    passwd='iamwithyou',
    db='mydb')
print("Database Connection Successful!!!")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO tblemp(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Anand', 'Lal', 32, 'M', 2590)"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()
print("Data Saved Successfully!!!")
# disconnect from server
db.close()
