
from django.contrib import admin
from django.urls import path
from app0 import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('main/',views.main,name='main'),
    path('',views.home, name='home'),
    path('loginhome/',views.loginhome,name='loginhome'),
    path('signuphome/',views.signuphome, name='signuphome'),
    path('logout/',views.logout, name='logout'),
    path('newitem/', views.newitem, name ='newitem'),
    
]
