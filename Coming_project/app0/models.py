from django.db import models
from datetime import datetime

class category(models.Model):
    objects = models.Manager()
    Plc = models.CharField(max_length=15,default="보관장소")

class item(models.Model):
    objects = models.Manager()
    img = models.ImageField(upload_to="image", blank=True)
    name = models.CharField(max_length=15, default="이름")
    amount = models.IntegerField(default=1)
    date = models.DateTimeField(default=datetime.now, blank=True)
    exp = models.DateTimeField(default=datetime.now, blank=True)
    plc = models.ForeignKey('category', on_delete=models.CASCADE)

    def __str__(category):
        return category.name

    class Meta:
        ordering = ['date']