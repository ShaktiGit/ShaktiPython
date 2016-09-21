#http://www.tutorialspoint.com/python/python_sending_email.htm
import smtplib
sender='shakti.jena@techmahindra.com'
rcvr='sj00129012@techmahindra.com'
msg="This is a msg"

try:
    smtpobj=smtplib.SMTP('localhost')
    smtpobj.sendmail(sender,rcvr,msg)
    print("Email Sent Successfully!!!")
except Exception:
    print("Error in sending mail !!!!")
