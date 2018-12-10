from django.db import models

# Create your models here.


class Goods(models.Model):

    """
    商品模型
    id：主键，自动生成，可不写
    price：商品价格
    name：商品名称
    """
    name = models.CharField(max_length=300)
    price = models.FloatField()
    sales = models.IntegerField()
    address = models.CharField(max_length=300)

    def __str__(self):
        return '%s--%s' % (self.pk, self.name)

    class Meta():
        db_table = 'goods'
