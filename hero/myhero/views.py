import time
from django.core.files.images import ImageFile
from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.forms import Form
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.views.generic.base import View

from .models import BookInfo
from .models import HeroInfo
import os
from hero import settings
from hero import myutil


# Create your views here.


def index(request):
    return render(request, "index.html")


def book(request):
    book_list = BookInfo.objects.all()
    return render(request, "book.html", {"book_list": book_list})


class HeroListView(ListView):
    # def get(self, request):
    #     return render(request, "hero.html.bak")

    # model = HeroInfo

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['hero_list'] = HeroInfo.objects.all()
    #     return context

    # def get_template_names(self):
    #     return 'hero.html'
    #
    # def get_queryset(self):
    #     return HeroInfo.objects.all()
    #
    # def get_context_object_name(self, object_list):
    #     return 'hero_list'

    queryset = HeroInfo.objects.all()
    context_object_name = 'hero_list'
    template_name = 'hero.html'
    # 分页
    paginate_by = 2


# 查询英雄
# def hero_page(request, page_now):
#     time.sleep(2)
#     # 每一页的条数
#     page_size = 2
#     hero_list = HeroInfo.objects.all()
#     # 创建Paginator对象
#     my_paginator = Paginator(hero_list, page_size)
#     # 创建Page对象
#     my_page = my_paginator.page(page_now)
#
#     hero_list = []
#     # for hero in my_page.object_list:
#     #     hero_list.append({"id": hero.id, "hname": hero.hname})
#     hero_list = serialize('json',my_page.object_list,ensure_ascii=False)
#     print(hero_list)
#     # print(my_paginator.page_range)
#     # print(my_page.number)
#     context = {
#         "hero_list": hero_list,
#         "page_list": list(my_paginator.page_range),
#         "page_now": my_page.number,
#         "page_prev": my_page.has_previous(),
#         "page_next": my_page.has_next(),
#     }
#     return JsonResponse(context)
#     # return render(request, 'hero.html.bak.bak.bak', context)


# 删除英雄
class HeroDeleteView(DeleteView):
    # def get(self, request, id):
    #     if HeroInfo.objects.filter(id=id).exists():
    #         hero = HeroInfo.objects.get(id=id)
    #         # print(hero)
    #         hero.delete()
    #         # 重定向到hero方法
    #         return redirect("/myhero/hero_list")
    #     else:
    #         return HttpResponse("该英雄不存在")

    queryset = HeroInfo.objects.all()
    success_url = '/myhero/hero_list'
    template_name = 'hero_delete.html'
    context_object_name = 'hero'


class HeroEditView(UpdateView):
    # def get(self, request, id):
    #     context = {}
    #     try:
    #         hero = HeroInfo.objects.get(id=id)
    #         book_list = BookInfo.objects.all()
    #         upload_error = request.COOKIES.get("upload_error")
    #         if upload_error:
    #             context["upload_error"] = "上传失败"
    #         context["hero"] = hero
    #         context["book_list"] = book_list
    #     except HeroInfo.DoesNotExist:
    #         pass
    #     return render(request, "hero_edit.html", context)
    #
    # def post(self, request, id):
    #     if HeroInfo.objects.filter(id=id).exists():
    #         hero = HeroInfo.objects.get(id=id)
    #         # print(hero)
    #         request_post = request.POST
    #         hero.hname = request_post.get("hname")
    #         hero.hage = request_post.get("hage")
    #         hero.hgender = int(request_post.get("hgender"))
    #         hero.hdesc = request_post.get("hdesc")
    #
    #         # ImageFile类继承File类，扩展了width和height属性
    #         file_hpic = ImageFile(request.FILES["hpic"])
    #         # 检查文件的格式、大小、宽高
    #         # if file_hpic.name.endswith(".jpg") and round(file_hpic.size / 1024, 1) <= 300 \
    #         #     and 200 <= file_hpic.width <= 300 and 200 <= file_hpic.height <= 300:
    #         file_name = myutil.do_file_name(file_hpic.name)
    #         file_path = os.path.join(settings.MEDIA_ROOT, "book", file_name)
    #         # 文件上传1--上传到服务器
    #         with open(file_path, "wb") as file:
    #             for chunk in file_hpic.chunks():
    #                 file.write(chunk)
    #
    #         # 文件上传2--写入到数据库中
    #         hero.hpic = os.path.join("book", file_name)
    #
    #         if request_post.get("hbook_id") == "0":
    #             hero.hbook_id = None
    #         else:
    #             hero.hbook_id = int(request_post.get("hbook_id"))
    #         hero.save()
    #
    #         response = redirect("/myhero/hero")
    #     # else:
    #     #     response = redirect("/myhero/hero_edit/" + id)
    #     #     response.set_cookie("upload_error", 1)
    #         return response
    #     else:
    #         return HttpResponse("该英雄不存在")

    queryset = HeroInfo.objects.all()
    template_name = 'hero_edit.html'
    success_url = '/myhero/hero_edit'
    fields = ['hname', 'hage', 'hgender', 'hdesc', 'hpic', 'hbook']
    context_object_name = 'hero'
    extra_context = {'book_list': BookInfo.objects.all()}

    def get_context_object_name(self, obj):
        return self.context_object_name

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name, context=self.extra_context)


    def post(self, request, *args, **kwargs):
        hero = HeroInfo()
        hero.hname = request.POST['hname']
        hero.hage = request.POST['hage']
        hero.hgender = request.POST['hgender']
        hero.hdesc = request.POST['hdesc']
        hero.hpic = request.FILES['hpic']
        hero.save()
        return redirect('/myhero/hero_list')


class HeroAddView(CreateView):
    # def get(self, request):
    #     context = {}
    #     book_list = BookInfo.objects.all()
    #     upload_error = request.COOKIES.get("upload_error")
    #     if upload_error:
    #         context["upload_error"] = "上传失败"
    #     context["book_list"] = book_list
    #     return render(request, "hero_edit.html", context)
    #
    # def post(self, request):
    #     hero = HeroInfo()
    #     request_post = request.POST
    #     hero.hname = request_post.get("hname")
    #     hero.hage = request_post.get("hage")
    #     hero.hgender = int(request_post.get("hgender"))
    #     hero.hdesc = request_post.get("hdesc")
    #
    #     # 文件上传到服务器
    #     # ImageFile类继承FILE类，扩展了width、height属性
    #     file_hpic = ImageFile(request.FILES["hpic"])
    #     # print(file_hpic.name)
    #     # print(file_hpic.size)
    #     # print(file_hpic.width)
    #     # print(file_hpic.height)
    #     # if file_hpic.name.endswith(".jpg") and round(file_hpic.size // 1024, 1) <= 300 \
    #     #     and 200 <= file_hpic.width <= 300 and 200 <= file_hpic.height <= 300:
    #     file_name = myutil.do_file_name(file_hpic.name)
    #     file_path = os.path.join(settings.MEDIA_ROOT, "book", file_name)
    #     with open(file_path, "wb") as file:
    #         for chunk in file_hpic.chunks():
    #             file.write(chunk)
    #
    #     # 文件写入到数据库中
    #     hero.hpic = os.path.join("book", file_name)
    #
    #     if request_post.get("hbook_id") == "0":
    #         hero.hbook_id = None
    #     else:
    #         hero.hbook_id = int(request_post.get("hbook_id"))
    #     hero.save()
    #
    #     return redirect("/myhero/hero")
        # else:
        #     return render(request, "hero_edit.html", {"upload_error": "上传失败"})

    queryset = HeroInfo.objects.all()
    template_name = 'hero_add.html'
    success_url = '/myhero/hero_list/'
    fields = ['hname', 'hage', 'hgender', 'hdesc', 'hpic', 'hbook']
    extra_context = {'book_list': BookInfo.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = BookInfo.objects.all()
        return context

    def form_valid(self, form):
        # form.save()
        # return redirect(self.success_url)
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name, context=self.extra_context)

    def post(self, request, *args, **kwargs):
        # print(request.POST)
        # form = Form(request.POST, request.FILES)
        # print(form)
        # if form.is_valid():
        hero = HeroInfo()
        hero.hname = request.POST['hname']
        hero.hage = request.POST['hage']
        hero.hgender = request.POST['hgender']
        hero.hdesc = request.POST['hdesc']
        hero.hpic = request.FILES['hpic']
        hero.save()
        return redirect('/myhero/hero_list')
        # else:
        #     return HttpResponse('输入错误')

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     form.save()
    #     return redirect(self.success_url)





