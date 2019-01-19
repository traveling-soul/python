from  django.utils import deprecation
from django.http import HttpResponse
from . import settings


# 定义的中间件需要继承deprecation.MiddlewareMixin
class FilterIp(deprecation.MiddlewareMixin):
    def process_request(self, request):
        # print("process_request....")
        # return HttpResponse("您被禁止了访问")
        if request.META.get("HTTP_X_FORWARD_FOR"):
            ip = request.META["HTTP_X_FORWARD_FOR"]
        else:
            ip = request.META["REMOTE_ADDR"]
            # print("process_request....%s" % ip)

        if ip in settings.FILTER_IPS:
            print("您已经被禁止了....")

        return None