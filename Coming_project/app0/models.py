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

