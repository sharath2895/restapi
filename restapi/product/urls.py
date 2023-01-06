from django.contrib import admin
from django.urls import path, include
from product import views
from product import urls

urlpatterns = [
    path('product', views.product),
   
]