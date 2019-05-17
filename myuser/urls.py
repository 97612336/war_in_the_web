from django.urls import path

from myuser import views

myuser_urls = [
    path('register/', views.myregister),
    path('login/', views.mylogin),
]
