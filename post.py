
# post.py
# author : chenxi
#coding:utf-8


import urllib
import urllib2
import cookielib
import re

class Login:
        url = 'http://www.cdjwc.com/jiaowu/Login.aspx'
        logout_url='http://www.cdjwc.com/jiaowu/other/Logout.asp'
        headers={
                "Accept":"text/html, application/xhtml+xml, image/jxr, */*",
                "Refere":"http://www.cdjwc.com/jiaowu/",
                "Accept-Language":"en-CA,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586",
                "Content-Type":"application/x-www-form-urlencoded",
                "Accept-Encoding":"gzip, deflate",
                "Host":"www.cdjwc.com"
                }
        data = {
                '__VIEWSTATE':'/wEPDwUKLTY2NzUxNzg0OQ9kFgICAw9kFgYCAg8PFgIeBFRleHRlZGQCBg8PFgIfAGVkZAIHDw8WAh8ABQMyNTJkZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAQUHQ2hrVXNlcl4iFL0IB4TFnW7rc1zW6Zmu0GHv',
                '__EVENTVALIDATION':'/wEWBQLcjciCBQKvo8HwCwKG85bvBgLAiqigBwKZwO3DDQhcnvKjEfdVQa+uecJ7IBS3R9Ey',
                'Account':'xxxxxxx',
                'PWD':'xxxxxxx',
                'cmdok':''
                }

        def __init__(self,UserId,UserPwd,SelectUrl):
                self.UserId = UserId
                self.UserPwd = UserPwd
                try:
                        Login.data.update({'Account':self.UserId,'PWD':self.UserPwd})
                        post_data = urllib.urlencode(Login.data)
                        cookieJar=cookielib.CookieJar()
                        self.opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
                        req=urllib2.Request(Login.url,post_data,Login.headers)
                        result=self.opener.open(req)
                        result=self.opener.open(SelectUrl)
                        self.StuScore=result.read()
                except Exception:
                        pass
        def Score_filter(self):
                #正则表达式获取成绩表格
                handel = re.compile(r'<table id="cjxx"(?:(?!<\/table>)[\s\S])*<\/table>')
                self.lists = handel.findall(self.StuScore)
                #将列表转成字符串
                self.s = "".join(list(self.lists))
                return self.s

        def Kb_filter(self):
                #正则表达式获取课程表
                handel = re.compile(r'<table border=1(?:(?!<\/table>)[\s\S])*<\/table>')
                self.lists = handel.findall(self.StuScore)
                #将列表转成字符串
                self.s = "".join(list(self.lists))
                self.opener.open(Login.logout_url)
                self.opener.close()
                return self.s

        def __del__(self):
                pass
