from django.db import models


# Create your models here.


class Army():
    def __init__(self):
        self.name = ''
        self.attract_num = 0
        self.defen_num = 0
        self.speed_num = 0
        self.cost_num = 0
        self.trans_num = 0

    @staticmethod
    def create_army(name, attract_num, defen_num, speed_num, cost_num, trans_num):
        army = Army()
        army.name = name
        army.attract_num = attract_num
        army.defen_num = defen_num
        army.speed_num = speed_num
        army.cost_num = cost_num
        army.trans_num = trans_num
        return army
