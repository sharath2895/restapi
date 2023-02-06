# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from .serializers import OrderCreationSerializer
from .models import Orders
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class OrderListView(generics.GenericAPIView):
    serializer_class = OrderCreationSerializer
    queryset = Orders.objects.all()
    permission_classes=[IsAuthenticated]
    def get(self, request):
        orders = Orders.objects.all()
        serializer = self.serializer_class(instance=orders, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        user = request.user
        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(generics.GenericAPIView):

    def get(self, request, order_id):
        pass

    def put(self, request, order_id):
        pass

    def delete(self, request, order_id):
        pass
