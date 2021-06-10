from django.contrib import admin
from django.urls import path, include
import Youtube

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Youtube/', include('Youtube.urls')),
    path('phoneinspace/', include('phoneinspace.urls')),
    path('', include('inw.urls')),

]
