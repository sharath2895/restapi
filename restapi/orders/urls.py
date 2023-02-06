from django.contrib import admin
from django.urls import path, include
from product import views
from product import urls
from authentication import urls as authurls
from .views import OrderListView


urlpatterns = [
    path('', OrderListView.as_view(), name='order-list')
]
