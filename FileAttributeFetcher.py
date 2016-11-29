#http://effbot.org/zone/python-fileinfo.htm
import os, time,datetime,socket
from stat import *


try:
    ipaddr=socket.gethostbyname(socket.gethostname())
    logfile=open('F:\\tech mahindra\\ALL\\python\\pycsvfiles\\pycsvlog.txt','a')
    st = os.stat('F:\\tech mahindra\\ALL\\python\\pycsvfiles\\student.csv')
    print("file size in bytes:", st[ST_SIZE])
    print("file modified:", time.asctime(time.localtime(st[ST_MTIME])))
    print("file created:", time.asctime(time.localtime(st[ST_CTIME])))
    print("file last accessed:", time.asctime(time.localtime(st[ST_ATIME])))
    logfile.write("file size in bytes:")
    fsize=str(st[ST_SIZE])
    fmodifytime=str(time.asctime(time.localtime(st[ST_MTIME])))
    print("fmodifytime: ",fmodifytime)
    fcreatetime=str(time.asctime(time.localtime(st[ST_CTIME])))
    print("fcreatetime: ",fcreatetime)
    faccesstime=str(time.asctime(time.localtime(st[ST_CTIME])))
    fipaddr=str(ipaddr)
    print("faccesstime: ",faccesstime)
    logfile.write("******")
    logfile.write("IP Address:")
    logfile.write(fipaddr)
    print("fipaddr: ",fipaddr)
    logfile.write("current date and time:")
    logfile.write(str(datetime.datetime.now()))
    logfile.write("file size in bytes:")
    logfile.write(fsize)
    logfile.write("file modify time:")
    logfile.write(fmodifytime)
    logfile.write("file creation time:")
    logfile.write(fcreatetime)
    logfile.write("file last accessed time:")
    logfile.write(faccesstime)

    logfile.write("******")
    print("Logs Written Successfully!!!")
    
except:
    print("failed to get information about the file !!")
