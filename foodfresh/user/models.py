from db.base_model import BaseModel
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class UserInfo(AbstractUser, BaseModel):

    class Meta():
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class EmailVerifyRecord(models.Model):
    # 激活码
    code = models.CharField(max_length=30)
    email = models.EmailField()
    # 邮件类型
    send_type = models.CharField(max_length=50)

    class Meta:
        db_table = 'emailverify'


class Address(BaseModel):
    '''地址模型类'''
    user = models.ForeignKey('UserInfo', verbose_name='所属用户', on_delete=True)
    receiver = models.CharField(max_length=20, verbose_name='收件人')
    addr = models.CharField(max_length=256, verbose_name='收件地址')
    zip_code = models.CharField(max_length=6, null=True, verbose_name='邮政编码')
    phone = models.CharField(max_length=11, verbose_name='联系电话')
    is_default = models.BooleanField(default=False, verbose_name='是否默认')

    class Meta:
        db_table = 'address'
        verbose_name = '地址'
        verbose_name_plural = verbose_name


