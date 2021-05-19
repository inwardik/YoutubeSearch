from django.contrib import admin
from django.urls import path, include
import Youtube

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Youtube.urls'))

]
