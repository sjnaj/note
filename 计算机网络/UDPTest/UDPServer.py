'''
Author: fengsc
Date: 2022-04-19 15:15:32
LastEditTime: 2022-04-19 22:17:37
'''
from socket import *
import traceback
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
try:
    serverSocket.bind(('', serverPort))  # 注意参数为元组,Symbolic name ('') meaning all available interfaces
except error as msg:
    print('Bind failed')
    print(repr(msg))
    exit()
    #traceback.print_exc()#错误位置和基本信息并退出
    #print(sys.exc_info())#获取完整信息而不打断

print("The server is ready to receive")
while True:  # 不断接收
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
