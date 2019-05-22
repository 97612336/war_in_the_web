import datetime
import logging

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from map.models import get_random_x_y, Map
from myuser.models import Myuser


# 给用户随机生成一个坐标
def set_user_location(user_id):
    x, y = get_random_x_y()
    m = Map()
    m.x_num = x
    m.y_num = y
    m.blong_to = user_id
    m.building = 1  # 1代表主城
    m.save()


# 用户注册
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
        # 用户注册成功，然后生成一个坐标给用户使用
        set_user_location(u.id)
        return HttpResponse('注册成功%s,%s' % (u.id, u.username))
    else:
        return HttpResponse("参数不合法")


# 　用户登录
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
