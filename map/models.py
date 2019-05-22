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
    building_id = models.IntegerField(default=0)  # 对应的建筑id

    class Meta:
        db_table = 'map'
        unique_together = ('x_num', 'y_num')
        index_together = ('blong_to', 'building_id')


# 建筑表
# 1代表主城，２代表军营，３代表农田，４代表牧场,5代表市场
class Building(models.Model):
    name = models.CharField(max_length=50)  # 建筑名称
    blong_to = models.IntegerField(default=0)  # 属于谁
    grade = models.IntegerField()  # 建筑等级
    hp_num = models.IntegerField(default=100)  # 建筑血量

    class Meta:
        db_table = 'building'

    # 获取主城
    def get_main_cuty(self, user_id, grade_num):
        b = Building()
        b.name = "主城"
        b.blong_to = user_id
        b.grade = grade_num
        b.hp_num = grade_num * 10000
        return b

    # 获取军营
    def get_camp(self, user_id, grade_num):
        b = Building()
        b.name = "军营"
        b.blong_to = user_id
        b.grade = grade_num
        b.hp_num = grade_num * 8000
        return b

    # 获取农田
    def get_farm(self, user_id, grade_num):
        b = Building()
        b.name = "农田"
        b.blong_to = user_id
        b.grade = grade_num
        b.hp_num = grade_num * 7000
        return b

    # 获取牧场
    def get_pasture(self, user_id, grade_num):
        b = Building()
        b.name = "牧场"
        b.blong_to = user_id
        b.grade = grade_num
        b.hp_num = grade_num * 7000
        return b

    # 获取市场
    def get_market(self, user_id, grade_num):
        b = Building()
        b.name = "市场"
        b.blong_to = user_id
        b.grade = grade_num
        b.hp_num = grade_num * 7000
        return b



