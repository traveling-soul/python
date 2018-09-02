from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


class BookInfo(models.Model):
    bname = models.CharField(max_length=30)


class HeroInfo(models.Model):
    hname = models.CharField(max_length=30)
    hage = models.IntegerField()
    hgender = models.BooleanField()
    hdesc = models.CharField(max_length=200)
    hbook = models.ForeignKey('BookInfo', on_delete=True, null=True)
