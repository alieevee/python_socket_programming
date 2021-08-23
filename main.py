import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname('www.google.com')

print(ip)

port = 80
s.connect((ip, port))

print("The socket has successfully connected to Google on IP Address == %s" %(ip))

message = "GET / HTTP/1.1\r\n\r\n"
s.sendall(message.encode('utf-8'))
print("Message send successfully")

reply = s.recv(4096)
print(reply)

s.close()
