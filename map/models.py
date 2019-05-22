import random

from django.contrib.admin import register
from django.db import models

# Create your models here.

# 地图表
from django.db.models import Q

from war_in_the_web.log import logger


class Map(models.Model):
    x_num = models.IntegerField()
    y_num = models.IntegerField()
    blong_to = models.IntegerField(default=0)  # 属于谁,user_id
    building = models.IntegerField(default=0)  # 地图上的建筑类型,building_id

    class Meta:
        db_table = 'map'
        unique_together = ('x_num', 'y_num')
        index_together = ('blong_to', 'building')


# 建筑表
class Building(models.Model):
    name = models.CharField(max_length=50)
    blong_to = models.IntegerField(default=0)
    grade = models.IntegerField()

    class Meta:
        db_table = 'building'


# 得到地图中已经存在的地图坐标
map_list = []
map_res = Map.objects.filter(~Q(blong_to=0)).filter(~Q(building=0)).all()
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
