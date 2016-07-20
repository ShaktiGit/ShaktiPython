import socket
ipaddr=socket.gethostbyname(socket.gethostname())
print("IP Address: ",ipaddr)
print("Now printing the socket name for Gmail Port 80....")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com",80))
print("Socket Name: ",s.getsockname()[0])
s.close()
