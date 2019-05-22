from django.urls import path

from map import views

map_urls = [
    path('test/', views.create_x_y_map),
]
