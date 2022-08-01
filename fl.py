import smtplib,random
from email.mime.text import MIMEText
from threading import Thread
# Thread(None,lambda:print(),None).start()
smtp_server = 'zlcython.top'
sender = 'lucas@zlcython.top'
password = 'zlc20100303'
receiver='teacherj@zlcython.top'
def get_random():
    out=''
    for i in range(5):
        out+=str(random.choice('1234567890-=`qwertyuiop[]\asdfghjkl;\'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?"'))
    return out
def makemsg(sub,massage,from_=None,to=None):
    # 创建SMTP对象
    msg = MIMEText(massage, 'plain', _charset="utf-8")
    # 邮件主题描述
    msg["Subject"] = sub
    # 发件人显示，不起实际作用
    msg["from"] = from_
    # 收件人显示，不起实际作用
    msg["to"] = to
    return msg
smtp = smtplib.SMTP()
with smtp as s:
    # 连接服务器
    s.connect(smtp_server)
    # 登录邮箱账号
    s.login(sender, password)
    for i in range(50):
        Thread(None,lambda:s.sendmail(sender, receiver, makemsg('测试邮件'+get_random(),'测试邮件内容'+get_random()).as_string()),None).start()