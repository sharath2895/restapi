from django.contrib import admin
from django.urls import path, include
from .views import Events, ClubAttendeeView, EventDetailView


urlpatterns = [
    path('', Events.as_view(), name='events'),
    path('event-detail/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event-detail/', EventDetailView.as_view(), name='event-detail'),
    path('create-attendee/', ClubAttendeeView.as_view(), name='create-attendee'),
    path('attendee/<int:pk>/', ClubAttendeeView.as_view(), name='attendee'),
]
