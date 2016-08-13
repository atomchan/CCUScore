# Server_socket_code
# encoding=utf-8
# author:陈熙

import socket

ClientSockst = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ClientSockst.connect(('127.0.0.1',8020))
print u'请输入学号:'
UserId = raw_input()
ClientSockst.send(UserId)
print u'请输入密码:'
UserPwd =raw_input()
ClientSockst.send(UserPwd)
print u'请输入邮箱:'
email =raw_input()
ClientSockst.send(email)
print u'1.查看成绩\n2.查看课表\n'
select =raw_input()
ClientSockst.send(select)

massage1 = ClientSockst.recv(1024)
print u'服务器返回:',massage1.decode("utf-8")
massgse2 = ClientSockst.recv(1024)
print u'服务器返回:',massgse2.decode("utf-8")
massgse3 = ClientSockst.recv(1024)
print u'服务器返回:',massgse3.decode("utf-8")
massgse4 = ClientSockst.recv(1024)
print u'服务器返回:',massgse4.decode("utf-8")
ClientSockst.close()