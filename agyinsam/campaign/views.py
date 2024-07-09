from django.shortcuts import render
from .models import Policy, Event, Upcoming_events
from datetime import date

def home(request):
    return render(request, 'campaign/home.html')

def policies(request):
    policies = Policy.objects.all()
    return render(request, 'campaign/policies.html', {'policies': policies})

def events(request):
    events = Event.objects.all()
    return render(request, 'campaign/events.html', {'events': events})

def upcoming_events(request):
    upcoming_events = Upcoming_events.objects.filter(date__gte=date.today())
    return render(request, 'campaign/upcoming_events.html', {'upcoming_events': upcoming_events})
