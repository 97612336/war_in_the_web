import random
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from war_in_the_web.log import logger


def create_x_y_map(request):
    return HttpResponse('哈哈哈')
