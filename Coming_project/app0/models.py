from django.db import models
from datetime import datetime


class category(models.Model):
    Plc = models.CharField(max_length=15,default="보관장소")

class item(models.Model):
    objects = models.Manager()
    img = models.ImageField(upload_to = "image", blank=True)
    name = models.CharField(max_length=15,default="이름")
    amount = models.CharField(max_length=1000,default=1,blank=True)
    date = models.DateTimeField(default=datetime.now,blank=True)
    exp = models.DateTimeField(default=datetime.now,blank=True)
    plc = models.ForeignKey(category, on_delete=models.CASCADE)

class User(models.Model):
    username = models.CharField(max_length=50, verbose_name = '사용자명')
    password = models.CharField(max_length=200, verbose_name = '비밀번호')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    updated_at = models.DateTimeField(auto_now=True)
           
    class Meta:
        db_table = 'User'