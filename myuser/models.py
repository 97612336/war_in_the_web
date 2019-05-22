import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Myuser(AbstractUser):
    user_kind = models.IntegerField(default=0)
    register_datetime = models.DateTimeField()

    class Meta:
        db_table = 'myuser'
