from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import CreateView
from polls.forms import QuestionForm


class QuestionCreate(CreateView):
    form_class = QuestionForm  # 表类
    template_name = 'question_form.html'  # 添加表对象的模板页面
    success_url = '/mypolls/thanks'  # 成功添加表对象后 跳转到的页面

    def form_invalid(self, form):  # 定义表对象没有添加失败后跳转到的页面。
        return HttpResponse("form is invalid.. this is just an HttpResponse object")

    # 此方法重写后，不能自动存入数据库
    # def form_valid(self, form):
    #     return redirect(self.success_url)

class ThanksView(View):
    def get(self, request):
        return render(request, 'thanks.html')