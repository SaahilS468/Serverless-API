from django.contrib import admin
from django.urls import path
from .views import home, getPainting

urlpatterns = [
    path('', home, name="home"),
    path('paintings/', getPainting, name="painting"),
]