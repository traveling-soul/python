# coding:utf-8

import smtplib, datetime, sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

username = "1335036337"

_user = "traveling_soul@163.com"
# 授权码，不是密码
_pwd = "1994gaowei689"
_to_list = ["%s@qq.com" % username]

msg = MIMEMultipart()

# 设置邮件编码
msg["Accept-Language"] = "zh-CN"
msg["Accept-Charset"] = "ISO-8859-1,utf-8"

# 邮件标题
msg["Subject"] = u"django文件"
msg["From"] = _user
msg['to'] = ','.join(_to_list)

# 内容部分
part = MIMEText("""
    你好 \n
    你的VPN帐号已经开通正常 \n
    帐号：%s \n
    压缩包密码：imay \n
    使用教程请看附件 \n
    """ % username, _charset="utf-8")
msg.attach(part)

# 附件部分
part = MIMEApplication(open("D:/BaiduNetdiskDownload/django.docx",'rb').read())
part.add_header('Content-Disposition', 'attachment', filename="D:/BaiduNetdiskDownload/django.docx")
msg.attach(part)

# 使用SSL协议进行发送邮件
server = smtplib.SMTP_SSL()
server.connect("smtp.163.com", 465)
server.set_debuglevel(1)
server.login(_user, _pwd)
server.sendmail(_user, _to_list, msg.as_string())
server.close()
