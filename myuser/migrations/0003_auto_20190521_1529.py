# Generated by Django 2.1.4 on 2019-05-21 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0002_auto_20190521_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='register_datetime',
            field=models.DateTimeField(default='2010-10-20 00:00:00'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='user_kind',
            field=models.IntegerField(default=0),
        ),
    ]
