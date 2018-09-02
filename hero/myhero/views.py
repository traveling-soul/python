import random
from io import BytesIO

from PIL import Image, ImageFont, ImageDraw
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import BookInfo
from .models import HeroInfo
from .models import UserInfo


# Create your views here.


def login(request):
    return render(request, "login.html")


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
    request.session.set_expiry(0)

    return HttpResponse(buf.getvalue(), 'image/png')


def login_handler(request):
    request_post = request.POST
    verificationcode = request_post.get("verificationcode")
    if request.session["verificationcode"].lower() != verificationcode.lower():
        code_error = "验证码错误"
        return render(request, "login.html", {"code_error": code_error})

    uname = request_post.get("uname")
    upwd = request_post.get("upwd")

    try:
        user = UserInfo.objects.get(username=uname)
        if upwd == user.password:
            return render(request, "index.html")
        else:
            pwd_error = "密码错误"
            return render(request, "login.html", {"pwd_error": pwd_error})
    except Exception:
        name_error = "账号错误"
        return render(request, "login.html", {"name_error": name_error})


def index(request):
    return render(request, "index.html")

def book(request):
    book_list = BookInfo.objects.all()
    return render(request, "book.html", {"book_list": book_list})


def hero(request):
    hero_list = HeroInfo.objects.all()
    return render(request, "hero.html", {"hero_list": hero_list})


def hero_delete(request, id):
    hero = HeroInfo.objects.get(id=id)
    # print(hero)
    hero.delete()
    return redirect("/myhero/hero")


def hero_edit(request, id):
    hero = HeroInfo.objects.get(id=id)
    book_list = BookInfo.objects.all()
    return render(request, "hero_edit.html", {"hero": hero, "book_list": book_list})


def hero_edit_handler(request, id):
    hero = HeroInfo.objects.get(id=id)
    # print(hero)
    request_post = request.POST
    hero.hname = request_post.get("hname")
    hero.hage = request_post.get("hage")
    hero.hgender = int(request_post.get("hgender"))
    hero.hdesc = request_post.get("hdesc")
    hero.hbook_id = request_post.get("hbook_id")
    hero.save()
    return redirect("/myhero/hero")


def hero_add(request):
    book_list = BookInfo.objects.all()
    return render(request, "hero_add.html", {"book_list": book_list})

def hero_add_handler(request):
    hero = HeroInfo()
    request_post = request.POST
    hero.hname = request_post.get("hname")
    hero.hage = request_post.get("hage")
    hero.hgender = int(request_post.get("hgender"))
    hero.hdesc = request_post.get("hdesc")
    if request_post.get("hbook_id") == "0":
        hero.hbook_id = None
    else:
        hero.hbook_id = int(request_post.get("hbook_id"))
    hero.save()

    return redirect("/myhero/hero")