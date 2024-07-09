from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('policies/', views.policies, name='policies'),
    path('events/', views.events, name='events'),
    path('upcoming-events/', views.upcoming_events, name='upcoming_events'),
]
