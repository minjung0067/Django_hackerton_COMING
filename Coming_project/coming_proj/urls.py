
from django.contrib import admin
from django.urls import path
from app0 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main,name="main"),
    path('newitem/',views.newitem, name="newitem"),
    path('newitem/<int:detail_id>',views.newitem, name="newitem"),
    
]
