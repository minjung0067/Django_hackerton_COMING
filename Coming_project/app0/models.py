from django.db import models
from datetime import datetime

class category(models.Model):
    objects = models.Manager()
    Plc = models.CharField(max_length=15,default="보관장소")

class item(models.Model):
    objects = models.Manager()
<<<<<<< HEAD
    img = models.ImageField(upload_to="image", blank=True)
=======
    img = models.ImageField(upload_to="image", blank=True ,null=True)
>>>>>>> master
    name = models.CharField(max_length=15, default="이름")
    amount = models.IntegerField(default=1)
    date = models.DateTimeField(default=datetime.now, blank=True)
    exp = models.DateTimeField(default=datetime.now, blank=True)
    plc = models.ForeignKey('category', on_delete=models.CASCADE)

    def __str__(category):
        return category.name

    class Meta:
        ordering = ['date']

class User(models.Model):
    username = models.CharField(max_length=64, verbose_name = '사용자명')
    password = models.CharField(max_length=64, verbose_name = '비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    def __str__(self):
        return self.username

        
    class Meta:
        db_table = 'test_user'