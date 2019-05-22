from django.contrib import admin

# Register your models here.
from map.models import Map, Building

admin.register(Map)
admin.register(Building)
