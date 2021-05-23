from django.contrib import admin
from django.urls import path
from .views import main_search


urlpatterns = [
    path('', main_search),
]
