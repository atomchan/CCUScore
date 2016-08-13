# author : 陈熙
# encoding:utf-8

import post
import ccuemail
import socket_server

class Score:
	def run_server(self):
		ser = socket_server.Server()
		print '运行。。'
		tup = ser.connect()
		UserId = tup[0]
		UserPwd = tup[1]
		email = tup[2]
		select = tup[3]
		table = ""
		#查看成绩的链接
		score_url='http://www.cdjwc.com/jiaowu/JWXS/cjcx/jwxs_cjcx_like.aspx'
		#查看课表的链接
		kb_url = 'http://www.cdjwc.com/jiaowu/JWXS/pkgl/xsxskb_xsy.aspx?xnxqh=2015-2016-2&sffd=1'
		try:
			if '1' == select:
				SelectUrl = score_url
				ser.received('正在提交...')
				user = post.Login(UserId,UserPwd,SelectUrl)
				table = user.Score_filter()
			elif '2' == select:
				SelectUrl = kb_url
				ser.received('正在提交...')
				user = post.Login(UserId,UserPwd,SelectUrl)
				table = user.Kb_filter()
			if not table:
				ser.received('你的学号或者密码出现错误，请重新输入')
			else:
				ser.received('提交成功...\n正在向用户发送邮件...')
				Send = ccuemail.SendEmail(table,email)
				#发送邮件
				ser.received(Send.send())
				Send.__del__()

		except Exception:
			ser.received('服务器压力过大')
		finally:
			ser.received('谢谢使用')
			ser.close_socket()

	def __del__(self):
		pass