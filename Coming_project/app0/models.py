from django.db import models

class item(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=15,default="이름")
    amount = models.IntegerField(default=1)
    date = models.DateField(auto_now=False)
    exp = models.DateTimeField(auto_now=False)
    plc = models.CharField(max_length=15,default="보관장소")