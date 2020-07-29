from django.contrib import admin
from .models import item,category,User
from django.contrib.auth.admin import UserAdmin

class categoryAdmin(admin.ModelAdmin):
    list_display = ['id','Plc']

class itemAdmin(admin.ModelAdmin):
    list_display = ['id','name','plc']


class UserAdmin(admin.ModelAdmin):
    list_display = ['name','password','created_at','updated_at']

admin.site.register(category,categoryAdmin)
admin.site.register(item,itemAdmin)