import datetime

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from map.util import create_one_city
from myuser.models import Myuser


def myregister(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    is_exit = Myuser.objects.filter(username=username).count()
    if is_exit:
        return HttpResponse('用户已经存在')
    if username and password:
        u = Myuser()
        u.username = username
        u.set_password(password)
        u.user_kind = 1
        u.register_datetime = datetime.datetime.now()
        u.save()
        # 注册成功之后,往地图表里插入一条数据
        x_num, y_num = create_one_city(u)
        return HttpResponse('注册成功%s,%s' % (x_num, y_num))
    else:
        return HttpResponse("参数不合法")


def mylogin(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    if username and password:
        one_user = authenticate(username=username, password=password)
        if one_user:
            login(request, one_user)
            return HttpResponse('登录成功')
        else:
            return HttpResponse('账号或密码错误')
    else:
        return HttpResponse('参数不合法')
