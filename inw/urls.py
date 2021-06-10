from django.contrib import admin
from django.urls import path
from .views import inw


urlpatterns = [
    path('', inw),
]
