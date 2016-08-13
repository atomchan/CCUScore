#Server_socket_code
#coding:utf-8
#author:陈熙


import socket
class Server:
    UserId = ''
    UserPwd = ''
    email =''
    select = ''
    ClientSocket =''
    ServerSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def __init__(self):
        print "等待客户端连接..."

    def connect(self):
        self.ServerSocket.bind(('127.0.0.1',4000))
        self.ServerSocket.listen(5)
        self.ClientSocket,addr = self.ServerSocket.accept()
        self.UserId = self.ClientSocket.recv(1024)
        self.UserPwd = self.ClientSocket.recv(1024)
        self.email = self.ClientSocket.recv(1024)
        self.select = self.ClientSocket.recv(1024)
        return self.UserId,self.UserPwd,self.email,self.select

    def received(self,massage):
        self.ClientSocket.send(massage)

    def close_socket(self):
        self.ClientSocket.close()
        self.ServerSocket.close()

    def __del__(self):
        pass
