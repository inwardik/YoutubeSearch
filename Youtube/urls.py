from django.contrib import admin
from django.urls import path
from .views import main_search, detail


urlpatterns = [
    path('', main_search),
    path('detail/', detail),
]
