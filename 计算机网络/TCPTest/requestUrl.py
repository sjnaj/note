'''
Author: fengsc
Date: 2022-04-19 22:23:34
LastEditTime: 2022-04-19 23:04:36
'''
from socket import *  # for sockets

# create an INET, STREAMing socket
try:
    s = socket(AF_INET, SOCK_STREAM)
except error:
    print('Failed to create socket')
    exit()

print('Socket Created')

host = 'www.zhihu.com'
port = 80

try:
   remote_ip = gethostbyname(host)
   #remote_ip ='220.181.38.251'

except gaierror:
    # could not resolve
    print('Hostname could not be resolved. Exiting')
    exit()

# Connect to remote server
s.connect((remote_ip, port))

print('Socket Connected to ' + host + ' on ip ' + remote_ip)

# Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"

try:
    # Set the whole string
    s.sendall(message.encode())
except error:
    # Send failed
    print('Send failed')
    exit()

print('Message send successfully')

# Now receive data
reply = s.recv(4096).decode()

print(reply)
