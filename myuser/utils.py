# 得到地图中已经存在的地图坐标
import random

from django.db.models import Q

from map.models import Map

map_list = []
map_res = Map.objects.filter(~Q(blong_to=0)).filter(~Q(building_id=0)).all()
for one in map_res:
    x_num = one.x_num
    y_num = one.y_num
    one_trup = (x_num, y_num)
    map_list.append(one_trup)


# 生成不在数据库中的随机坐标
def get_random_x_y():
    x = int(random.random() * 10000)
    y = int(random.random() * 10000)
    one_trup = (x, y)
    if one_trup in map_list:
        get_random_x_y()
    else:
        map_list.append(one_trup)
        return x, y
