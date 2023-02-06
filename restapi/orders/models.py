# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Orders(models.Model):

    SIZES = (('SMALL', 'small'), ('MEDIUM', 'medium'),
             ('LARGE', 'large'), ('EXTRA_LARGE', 'extra_large'))

    ORDER_STATUS = (('PENDING', 'pending'), ('INTRANSIT',
                    'in-transit'), ('COMPLETED', 'completed'))

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(max_length=20, choices=SIZES)
    status = models.CharField(
        max_length=20, choices=ORDER_STATUS, default=ORDER_STATUS[0])
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
