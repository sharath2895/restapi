# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from rest_framework.response import Response
# from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class CustomUser(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Email cannot be Empty.!"))

        email = self.normalize_email(email)

        new_user = self.model(email=email, **extra_fields)
        new_user.set_password(password)
        new_user.save()

        return new_user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Super user should have is staff as true"))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Super user should have is superuser as true"))

        if extra_fields.get('is_active') is not True:
            raise ValueError(_("Super user should have is active as true"))

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True, max_length=100)
    phone_number = models.CharField(unique=True, null=False,max_length=10)    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number']
    objects = CustomUser()
