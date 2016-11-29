# Generating reports from tblcsv and tblcsvlid
# Related to csvTblLoadStatus
import matplotlib.pyplot as plt
import pymysql
from matplotlib import style
# database connection
db =pymysql.connect(host='localhost',
    user='root',
    passwd='iamwithyou',
    db='mydb')
print("Database Connection Successful!!!")

lidlist=[]
ldtimelist=[]
roll_list=[]
#Getting the tblcsvlid lid and lidtime
fetchcursor = db.cursor()
sql = "SELECT lid,lidtime,roll FROM tblcsvlid"
rescount=0
try:
   # Execute the SQL command
   fetchcursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = fetchcursor.fetchall()
   for row in results:
       rescount=rescount+1
       lid = row[0]
       ldtime = row[1]
       roll=row[2]
       lidlist.append(lid)
       ldtimelist.append(ldtime)
       roll_list.append(roll)
       # Now print fetched result
       print ("LID=%s,Loading Time=%s" % \
             (lid, ldtime ))
except:
   print ("Error: unable to fecth data")

# disconnect from server
fetchcursor.close()
db.close()
print("lidlist:",lidlist)
print("lidtimelist:",ldtimelist)
print("Roll_list:",roll_list)
roll_list1=[]
roll_list2=[]
lidlist1=[]
for j in lidlist:
    p=int(j.strip('\'').strip('\''))
    #i.rstrip('\'"')
    print(float(j.strip('\"').strip('\'')))
    lidlist1.append(p)
for i in roll_list:
    a=float(i.strip('\"').strip('\''))
    #i.rstrip('\'"')
    print(float(i.strip('\"').strip('\'')))
    roll_list1.append(a)
    
    b=int(i.strip('\"').strip('\''))
    #i.rstrip('\'"')
    print(int(i.strip('\"').strip('\'')))
    roll_list2.append(b)
print("Plotting the graph......")
#plt.plot(lidlist,roll_list1,'ro')
#plt.plot(lidlist, [float(i) for i in roll_list], 'ro')
#plt.show()

# Plotting the values
style.use('ggplot')
plt.plot(lidlist,roll_list1,linestyle="dashed", marker="o", color="red")
plt.xlabel("LID --->")
plt.ylabel("LID Loading Time --->")
#title
plt.title("LID vs Load Time Graph")
plt.show()

# Bar Plotting
print("Printing the bar graph.....")
plt.xlabel("LID --->")
plt.ylabel("LID Loading Time --->")
#title
plt.title("LID vs Load Time Graph")
plt.bar(lidlist1,roll_list2,align='center',color='g')
plt.show()
print("Printing the Scatter Graph......")
plt.xlabel("LID --->")
plt.ylabel("LID Loading Time --->")
#title
plt.title("LID vs Load Time Graph")
plt.scatter(lidlist1,roll_list2,color='b')
plt.show()
