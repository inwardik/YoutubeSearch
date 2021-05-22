from django.contrib import admin
from django.urls import path
from .views import main_search, related_search


urlpatterns = [
    path('', main_search),
    path('related/', related_search),
]
