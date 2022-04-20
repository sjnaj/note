'''
Author: fengsc
Date: 2022-04-19 15:10:16
LastEditTime: 2022-04-19 22:15:58
'''
from socket import *
try:
    serverHost=gethostname()
except gaierror as msg:
    print('Hostname could not be resolved')
    print(repr(msg))
    exit()
serverPort=12000
setdefaulttimeout(10)#十秒为最大时延
try:
    clientSocket = socket(AF_INET, SOCK_DGRAM)#指示为ipv4和udp
except error as msg:
    print('Failed to create socket')    
    print(repr(msg))
    exit()
message =input("Input lowercase sentence:")
clientSocket.sendto(message.encode(),(serverHost,serverPort))
modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()