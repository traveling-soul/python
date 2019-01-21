import random
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import UserInfo
import hashlib
import re
from django.views.generic.base import View
# Create your views here.


def md5_pwd(pwd):
    md5 = hashlib.md5()
    md5.update(pwd.encode('utf-8'))
    return md5.hexdigest()


def verification_code(request):
    # with open("D:\env3\env1\hero\c罗.jpg", "rb") as f:
    #     return HttpResponse(f.read, "image/jpeg")
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    # im = Image.new('RGB', (width, height), bgcolor)
    im = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象
    font = ImageFont.truetype('simsun.ttc', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 创建内存读写的对象
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')

    # 放入session中
    request.session['verificationcode'] = rand_str
    return HttpResponse(buf.getvalue(), 'image/png')
    request.session.set_expiry(0)


class RegistView(View):
    def get(self, request):
        return render(request, "regist.html")

    def post(self, request):
        uname = request.POST["uname"]
        if len(uname) < 6:
            return render(request, "regist.html")
        upwd_temp = request.POST["upwd"]
        if re.match("^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{8,16}$", upwd_temp):
            upwd = md5_pwd(upwd_temp)
        else:
            return render(request, "regist.html")
        if UserInfo.objects.filter(username=uname).exists():
            return render(request, "regist.html")
        else:
            user = UserInfo()
            user.username = uname
            user.password = upwd
            user.save()
            return redirect("/user/login")


class LoginView(View):
    def get(self, request):
        print("login....")
        return render(request, "login.html")

    def post(self, request):
        request_post = request.POST
        verificationcode = request_post.get("verificationcode")
        if request.session["verificationcode"].lower() != verificationcode.lower():
            code_error = "验证码错误"
            return render(request, "login.html", {"code_error": code_error})

        uname = request_post.get("uname")
        upwd_temp = request_post.get("upwd")
        upwd = md5_pwd(upwd_temp)

        try:
            user = UserInfo.objects.get(username=uname)
            if upwd == user.password:
                return redirect("/myhero/index")
            else:
                pwd_error = "密码错误"
                return render(request, "login.html", {"pwd_error": pwd_error})
        except Exception:
            name_error = "账号错误"
            return render(request, "login.html", {"name_error": name_error})


# 退出系统
class LogutView(View):
    def get(self, request):
        return redirect("/user/login")


# 检查用户名是否存在，存在则返回1，否则返回0
def check_username(request):
    uname = request.GET["uname"]
    if UserInfo.objects.filter(username=uname).exists():
        return HttpResponse("1")
    else:
        return HttpResponse("0")