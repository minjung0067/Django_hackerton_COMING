from django.contrib import admin
from .models import item,category

# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    list_display = ['id','Plc']

class itemAdmin(admin.ModelAdmin):
    list_display = ['id','name','plc']

admin.site.register(category,categoryAdmin)
admin.site.register(item,itemAdmin)
