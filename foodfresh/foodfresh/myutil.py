import hashlib
from random import Random

from django.shortcuts import redirect
import string
from django.core.mail import send_mail
from  user.models import EmailVerifyRecord
from foodfresh import settings

# md5加密
def mymd5(pwd):
    my_md5 = hashlib.md5()
    my_md5.update(pwd.encode('utf-8'))
    return my_md5.hexdigest()


# 登录的装饰器，对游客的权限进行限制
def login_wrapper(func):
    def wrapper(request, *args, **kwargs):
        if request.session.get('login_name'):
            return func(request, *args, **kwargs)
        else:
            return redirect('/user/login')
    return wrapper


# 发送邮件
def random_str(randomlength=8):#生成随机字符串用于激活链接后缀
    str = ''
    chars = string.ascii_letters
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type="register"):#根据注册类型: 注册or找回密码来判断发哪种邮件
    email_record = EmailVerifyRecord()#每次发邮件记录都记录在EmailVerifyRecord的模型中,用于激活时判断是否有
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == "register": # 根据send_type定制发送内容
        email_title = "天天生鲜后台在线系统激活链接"
        email_body = "天天生鲜后台在线系统激活链接: http://127.0.0.1:8000/user/active/{}".format(code)
        send_status = send_mail(email_title, email_body, settings.EMAIL_FROM, [email,])
        if send_status:
            pass
