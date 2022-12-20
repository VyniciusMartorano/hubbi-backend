from rest_framework import serializers
from . import models as m
from django.contrib.auth.models import User


class ProdutoSerializer(serializers.ModelSerializer):
    foto = serializers.ImageField(use_url=True)

    class Meta:
        model = m.Produto
        fields = ('__all__')


class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Compra
        fields = ('__all__')


class CompraProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.CompraProduto
        fields = ('__all__')



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id','username', 'password')
