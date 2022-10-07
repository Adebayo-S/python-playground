""" Socket Programming """
import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # AF_INET : IPV4
    # SOCK_STREAM : Connection Oriented TCP Protocol
    #       (Connection established before data transfer)
    # socket.error thrown on error
except socket.error as err:
    print(f'socket creation failed with error {err}')

port = 80

try:
    host_ip = socket.gethostbyname('www.github.com') # get ip
    print(host_ip)
except socket.gaierror: # if this is returned, it means there's a problem with thw DNS
    print('error resolving the host')
    sys.exit()

s.connect((host_ip, port))
print(f'socket has successfully connected to Github on port == {host_ip}')
