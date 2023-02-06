# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# from django.shortcuts import render
# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework import status
# from .models import User
# from .serializers import UserSerializer

# # Create your views here.

# @AuthService()
# class AuthView(generics.GenericAPIView):
#     def get(self, request):
#         res = AuthService(request)
#         return Response(data={"message": 'Auth call'}, status=status.HTTP_200_OK)


# class UserCreateView(generics.GenericAPIView):
#     serializer_class = UserSerializer

#     def post(self, request):
#         data = request.data

#         serializer = self.serializer_class(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             print(serializer)
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)

#         return Response(data = serializer.errors, status = status.HTTP_400_BAD_REQUEST)