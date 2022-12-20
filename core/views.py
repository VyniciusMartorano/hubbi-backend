import sys, os
from django.shortcuts import render
from django.db import models
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from . import serializers as s
from . import models as m

class UserViewSet(viewsets.ModelViewSet):
    queryset = m.User.objects.using('default')
    serializer_class = s.UserSerializer


    @action(detail=False, methods=['get'])
    def get_user(self, *args, **kwargs):
        user_id = self.request.__dict__["_auth"]["user_id"]
        qs = User.objects.using('default').get(id=user_id)        

        serializer = s.UserSerializer(qs, many=False).data
        return Response(serializer)


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = m.Produto.objects.using('default')
    serializer_class = s.ProdutoSerializer



class CompraViewSet(viewsets.ModelViewSet):
    queryset = m.Compra.objects.using('default')
    serializer_class = s.CompraSerializer


class CompraProdutoViewSet(viewsets.ModelViewSet):
    queryset = m.CompraProduto.objects.using('default')
    serializer_class = s.CompraProdutoSerializer

