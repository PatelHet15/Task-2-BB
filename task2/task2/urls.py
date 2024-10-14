from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('brainybeemapp/', include('brainybeemapp.urls')), 
    path('', lambda request: HttpResponseRedirect('/brainybeemapp/add/')),  
]
