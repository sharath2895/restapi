from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import ProductModel
from .serializers import ProductSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response as res
from rest_framework import status
# Create your views here.


@api_view(['GET', 'POST','PUT','DELETE'])
def product(request):
    if request.method == 'GET':
        product = ProductModel.objects.all()
        serializer = ProductSerializer(product, many=True)
        return res(serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        post_serializer = ProductSerializer(data = request.data)        
        if post_serializer.is_valid():
            print(post_serializer.fields['id'])
            post_serializer.save()
            return res({'data':post_serializer.data},status =status.HTTP_201_CREATED)
        else:
            return res({'message':post_serializer.errors}, status= status.HTTP_400_BAD_REQUEST)
