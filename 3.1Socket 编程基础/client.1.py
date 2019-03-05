# -*- coding: UTF-8 -*-

import socket
import sys

#测试类
class Client:
    def __init__(self,host):
        self.host=host #待连接的远程主机的域名
    def connet(self): #连接方法
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as e:
            print("Failed to create socket. Error: %s"%e)
            sys.exit() #退出进程
        try:
            remote_ip = socket.gethostbyname(self.host)#根据域名获取ip
        except socket.gaierror:
            print('主机无法被解析')
            sys.exit() #退出进程
        try:
            s.connect((remote_ip,80))#连接
            message = b"GET / HTTP/1.1\r\n\r\n"
            s.sendall(message)#发送数据
            reply = s.recv(4096)#接收数据
            print(reply)
            s.close()#关闭连接
        except socket.error:
            sys.exit() #退出进程


if __name__ == '__main__':
    cl = Client('www.baidu.com')
    cl.connet()