'''
Author: fengsc
Date: 2022-04-19 16:10:45
LastEditTime: 2022-04-20 16:09:55
'''
import os
from socket import *
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
try:
    clientSocket.bind(('', serverPort))
except error as msg:
    print("failed to bind")
    print(repr(msg))
    os.system("lsof -i:8000")
    exit()
clientSocket.listen(1)  # 最大同时运行一个连接
print("The server is ready to receive")
while True:
    connectSocket, addr = clientSocket.accept()  # 创建专用连接
    print("connect to ",addr," successfully")
    message = connectSocket.recv(2048).decode()
    print("get: ",message)
    modifiedMessage = message.upper()
    connectSocket.sendall(modifiedMessage.encode())
    connectSocket.close()  # 发送完后关闭专用连接，可继续重新由请求建立连接
