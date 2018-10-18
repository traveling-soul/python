import random
from io import BytesIO
import re

from PIL import Image, ImageDraw, ImageFont
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import View
from foodfresh.myutil import mymd5, send_register_email
from user.models import Address
from django.conf import settings

from .models import EmailVerifyRecord
from .models import UserInfo
from food.models import GoodsSKU


# Create your views here.


class Register(View):
    def get(self, request):
        return render(request, 'register.html', {'title': '注册'})

    def post(self, request):
        uname = request.POST['user_name']
        upwd = request.POST['pwd']
        cpwd = request.POST['cpwd']
        uemail = request.POST['email']

        if UserInfo.objects.filter(username=uname).exists():
            response = render('register.html')
            return response

        user = UserInfo.objects.create_user(uname, uemail, upwd)
        user.is_active = 0
        user.save()
        # 发激活邮件
        send_register_email(uemail, 'register')
        # response = redirect('/user/login')
        response = HttpResponse('邮件已发送，经查看邮件激活账号')
        return response


class ActiveView(View):
    def get(self, request, active_code):
        all_reocrds = EmailVerifyRecord.objects.filter(code=active_code)
        if all_reocrds:
            for record in all_reocrds:
                email = record.email
                user = UserInfo.objects.get(email=email)
                user.is_active = True
                user.save()
        return HttpResponse('邮件已激活，可以登录了')
        # return render(request, 'login.html')


def check_uname(request):
    uname = request.GET.get('uname')
    if UserInfo.objects.filter(username=uname).exists():
        return HttpResponse(1)
    else:
        return HttpResponse(0)


def verification_code(request):
    width = 100
    height = 25
    # 创建画面对象
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


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html',{'title': '登录'})

    def post(self, request):
        request_post = request.POST
        uname = request_post.get('user_name')
        upwd = request_post.get('pwd')

        verificationcode = request_post.get('verificationcode')
        if request.session["verificationcode"].lower() != verificationcode.lower():
            response = redirect('/user/login')
            return response

        user = authenticate(username=uname, password=upwd)
        print(user)
        if user != None:
            if user.is_active:
                # 记录用户的登录状态
                login(request, user)
                # 获取登录后要跳转的地址，如果找不到默认跳转到首页
                next_url = request.GET.get('next', default=reverse('food:index'))
                # 跳转到next_url
                response = redirect('/food/index')
            else:
                response = redirect('/user/login')
        else:
            response = redirect('/user/login')
        return response


def user_response(request):
    name = request.GET.get('name','')
    pwd = request.GET.get('pwd','')
    pwd = mymd5(pwd)
    if UserInfo.objects.filter(username=name).exists():
        user = UserInfo()
        if user.is_active:
            return JsonResponse({'user_error': 0, 'active': 1})
        else:
            return JsonResponse({'user_error': 0, 'active': 0})
    else:
        return JsonResponse({'user_error':1})


def user_response(request):
    name = request.GET.get('name','')
    pwd = request.GET.get('pwd','')
    pwd = mymd5(pwd)
    if UserInfo.objects.filter(username=name).exists():
        user = UserInfo()
        if user.is_active:
            return JsonResponse({'user_error': 0, 'active': 1})
        else:
            return JsonResponse({'user_error': 0, 'active': 0})
    else:
        return JsonResponse({'user_error':1})


def code_response(request):
    verificationcode = request.GET.get('verificationcode')
    if request.session["verificationcode"].lower() != verificationcode.lower():
        return JsonResponse({'verificationcode_error':1})
    else:
        return JsonResponse({'verificationcode_error':0})


# @login_wrapper
class UserInfoView(View):
    def get(self, request):
        user = request.user
        
        conn = settings.REDIS_CONN

        history_key = 'history_%d' % user.id

		#获取用户最新浏览的5个商品的id       
        sku_ids = conn.lrange(history_key, 0, 4)
        
        #遍历获取用户浏览的商品信息
        goods_li = []
        for id in sku_ids:
            goods = GoodsSKU.objects.get(id=id)
            goods_li.append(goods)
        context = {
            'title': '用户中心', 
            'page': 'info',
            'goods_li': goods_li
        }
        return render(request, 'user_center_info.html', context)


# @login_wrapper
class UserOrderView(View):
    def get(self, request):
        context = {'title': '用户中心', 'page': 'order'}
        return render(request, 'user_center_order.html', context)


# @login_wrapper
class UserAddressView(View):
    def get(self, request):
        user = request.user
        address_list = Address.objects.filter(user=user)
        context = {'title': '用户中心', 'page': 'site', 'address_list': address_list}
        return render(request, 'user_center_site.html', context)

    def post(self, request):
        receiver = request.POST.get('receiver')
        addr = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')

        if not all([receiver, addr, phone]):
            return render(request, 'user_center_site.html', {'err_msg': '数据不完整'})

        if re.match('r^1[3|4|5|7|8][0-9]{9}$', phone):
            return render(request, 'user_center_address.html', {'err_msg': '手机格式不对'})

        # 获得当前登录的用户
        user = request.user
        try:
            address = Address.objects.get(user=user, is_default=True)
            address.is_default = False
            address.save()
        except Address.DoesNotExist:
            pass

        Address.objects.create(receiver=receiver,
                       addr=addr,
                       zip_code=zip_code,
                       phone=phone,
                       is_default=True,
                       user=user)
        return redirect(reverse('user:site'))


def site_response(request):
    address = Address.objects.get(is_default=True)
    address.is_default = False
    address.save()

    id = request.GET.get('id')
    print(id)
    address2 = Address.objects.get(id=id)
    address2.is_default = True
    address2.save()
    return HttpResponse(11111)



class EditAddressView(View):
    def get(self, request, id):
        try:
            address = Address.objects.get(id=id)
        except Address.DoesNotExist:
            pass
        # print(address)
        user = request.user
        address_list = Address.objects.filter(user=user)
        context = {'title': '用户中心', 'page': 'site', 'address_list': address_list, 'address': address}
        return render(request, 'user_center_site.html', context)

    def post(self, request, id):
        receiver = request.POST.get('receiver')
        addr = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')
        try:
            address = Address.objects.get(id=id)
            address.receiver = receiver
            address.addr = addr
            address.zip_code = zip_code
            address.phone = phone
            address.save()
        except Address.DoesNotExist:
            pass

        return redirect(reverse('user:site'))


def del_site(request, id):
    try:
        address = Address.objects.get(id=id)
        flag = address.is_default
        address.delete()
        if flag:
            a = Address.objects.all()[0]
            a.is_default = True
            a.save()
    except Address.DoesNotExist:
        pass

    return redirect(reverse('user:site'))



class ChangePwdView(View):
    def get(self, request):
        context = {'title': '用户中心', 'page': 'pwd'}
        return render(request, 'user_center_pwd.html', context)

    def post(self, request):
        user = request.user
        email = request.POST.get('email')
        old_pwd = request.POST.get('old_pwd')
        new_pwd = request.POST.get('new_pwd')

        try:
            u = UserInfo.objects.get(username=user)
            if u.email == email:
                if authenticate(username=user, password=old_pwd):
                    u.set_password(new_pwd)
                    u.save()
        except UserInfo.DoesNotExist:
            pass
        return redirect('/user/login')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('food:index'))

########################################################################
# def test(request):
#     # 不用模板
#     response = HttpResponse('test')
#     response.set_cookie('my_cookie', 'cookie value')
#     return response


def test(request):
    # 用模板
    response = render(request, 'test.html')
    response.set_cookie('name', 'laowang')
    return response
