'''
Author: fengsc
Date: 2022-04-19 16:10:35
LastEditTime: 2022-04-20 20:39:01
'''
from socket import *
try:
    serverName = gethostname()
except gaierror as msg:
    print('Hostname could not be resolved')
    print(repr(msg))
    exit()
serverPort = 12000
try:
    clientSocket = socket(AF_INET, SOCK_STREAM)  # 第二个参数udp是SOCK_DGRAM
except error as msg:
    print('Failed to create socket')
    print(repr(msg))
    exit()

setdefaulttimeout(10)  # 十秒为最大时延
try:
    clientSocket.connect((serverName, serverPort))
except error as msg:
    print('Failed to connect')
    print(repr(msg))
    exit()
sentence = input('Input lowercase sentence:')
# *udp为sendto，需要地址参数 send较sentall更保险，前者并不确定这次调用是否会全部发送完成
clientSocket.sendall(sentence.encode())
clientSocket.shutdown(SHUT_WR)  # 与java服务端交互时需要,适用于仅发送一次的情况
'''
SHUT_RD：关闭 socket 的输入部分，程序还可通过该 socket 输出数据。
SHUT_WR： 关闭该 socket 的输出部分，程序还可通过该 socket 读取数据。
SHUT_RDWR：全关闭。该 socket 既不能读取数据，也不能写入数据。
'''
modifiedSentence = clientSocket.recv(1024).decode()  # udp是recvfrom
print(modifiedSentence)
clientSocket.close()
