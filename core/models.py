from django.db import models
from django.contrib.auth.models import User



class Produto(models.Model):
    descricao = models.CharField(max_length=255, null=False, blank=False)
    foto = models.ImageField(null=False, blank=False)
    preco = models.FloatField(null=False, blank=False)

    class Meta:
        managed = False
        db_table = 'Produto'


class Compra(models.Model):
    descricao = models.CharField(max_length=255,null=False, blank=False)
    class Meta:
        managed = False
        db_table = 'Compra'


class CompraProduto(models.Model):
    num_compra = models.IntegerField(null=False, blank=False)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'CompraProduto'