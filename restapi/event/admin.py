from django.contrib import admin
from .models import Event, ClubAttendee, Venue
# Register your models here.

admin.site.register(Event)
admin.site.register(ClubAttendee)
admin.site.register(Venue)