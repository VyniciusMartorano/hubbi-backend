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

    @action(detail=False, methods=['post'])
    def get_produtos_by_user(self, *args, **kwargs):
        qs = m.Produto.objects.using('default')
        req = self.request.data

        user_id = req['user_id'] if 'user_id' in req else None

        if user_id: qs = qs.filter(user=user_id)
        serializer = s.ProdutoSerializer(qs, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)



class CompraViewSet(viewsets.ModelViewSet):
    queryset = m.Compra.objects.using('default')
    serializer_class = s.CompraSerializer


    @action(detail=False, methods=['post'])
    def get_requests_by_user(self, *args, **kwargs):
        qs = m.Compra.objects.using('default')
        req = self.request.data

        qs = qs.filter(user_id=req['user_id'])
        serializer = s.CompraSerializer(qs, many=True).data

        return Response(serializer, status=200)




class CompraProdutoViewSet(viewsets.ModelViewSet):
    queryset = m.CompraProduto.objects.using('default')
    serializer_class = s.CompraProdutoSerializer


    @action(detail=False, methods=['post'])
    def get_itens_by_request_id(self, *args, **kwargs):
        qs = m.CompraProduto.objects.using('default')
        qs_produtos = m.Produto.objects.using('default')
        req = self.request.data

        request_id = req['request_id'] if 'request_id' in req else None
        if request_id: 
            produtos = qs.filter(compra_id=request_id).values_list('produto')
            qs_produtos = qs_produtos.filter(id__in=produtos)
        
        serializer = s.ProdutoSerializer(qs_produtos, many=True).data   
        return Response(serializer, status=200)


    @action(detail=False, methods=['post'])
    def save_itens_compra(self, *args, **kwargs):
        req = self.request.data

        user_id = req['user_id'] if 'user_id' in req else None
        compra_id = req['compra_id'] if 'compra_id' in req else None
        itens = req['itens'] if 'itens' in req else None


        for item in itens:
            cp = m.CompraProduto(compra_id=compra_id,user_id=user_id, produto_id=item['id'])
            cp.save()

        return Response(data='OK', status=200)