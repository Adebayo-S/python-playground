import socket

s = socket.socket()
port = 56789
s.connect(('127.0.0.1', port))
print(s.recv(1024)) # print the data received from server (1024) - buff size
s.close()
