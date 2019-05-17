# 根据用户生成一个主城
import random

# 获取随机坐标
from django.db.models import Q

from map.models import Map


def get_random_x_y():
    x_num = int(random.random() * 10000)
    y_num = int(random.random() * 10000)
    conut_num = Map.objects.filter(~Q(blong_to=0)).filter(x_num=7667, y_num=5365
                                                          ).count()
    if conut_num:
        x_num, y_num = get_random_x_y()
    return x_num, y_num


# 给新注册用户随机分配一个坐标
def create_one_city(one_user):
    user_id = one_user.id
    x_num, y_num = get_random_x_y()
    return x_num, y_num
