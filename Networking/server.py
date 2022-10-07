import socket

# server has a bind() method - binds to a specific ip and port to listen to
#    incoming requests.
# listen() - server listens to incoming connection
# accept() - initiates connection
# close() - closes connection

s = socket.socket()
print('socket created')
port = 56789
s.bind(('', port)) # the ip is empty so it can listen to other requests from other pcs
print(f'socket binded to port{port}')
s.listen(5) # 5 reps the max no of connections to listen to.
print('socket listening......')
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    message = ('Thanks for connecting')
    c.send(message.encode()) # encode the string into bytes
    c.close()
