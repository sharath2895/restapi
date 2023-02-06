from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import Event, ClubAttendee


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        depth = 1


class ClubAttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubAttendee
        fields ='__all__'
        # fields = ['id', 'first_name', 'last_name', 'email']
        depth = 1
    