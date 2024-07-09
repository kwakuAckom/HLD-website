from django.contrib import admin
from .models import Policy, Event, Upcoming_events

# Register your models here.

admin.site.register(Policy)
admin.site.register(Event)
admin.site.register(Upcoming_events)
