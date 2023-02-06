# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Orders

# Register your models here.

admin.site.register(Orders)


# @admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_per_page = 100
    list_display = ['customer', 'size', 'status', 'quantity', 'created_at']
