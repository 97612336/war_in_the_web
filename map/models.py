from django.db import models


# Create your models here.

# 地图表
class Map(models.Model):
    x_num = models.IntegerField()
    y_num = models.IntegerField()
    blong_to = models.IntegerField(default=0)  # 属于谁,user_id
    building = models.IntegerField(default=0)  # 地图上的建筑类型,building_id

    class Meta:
        db_table = 'map'
        unique_together = ('x_num', 'y_num')


# 建筑表
class Building(models.Model):
    name = models.CharField(max_length=50)
    blong_to = models.IntegerField(default=0)
    grade = models.IntegerField()

    class Meta:
        db_table = 'building'
