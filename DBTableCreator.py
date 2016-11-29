#Creating a table
import pymysql
# Open database connection
db =pymysql.connect(host='localhost',
    user='root',
    passwd='iamwithyou',
    db='mydb')
print("Database Connection Successful!!!")
# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS TBLEMP")

# Create table as per requirement
sql = """CREATE TABLE TBLEMP (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)
print("Table TBLEMP created!!!")
# disconnect from server
db.close()
