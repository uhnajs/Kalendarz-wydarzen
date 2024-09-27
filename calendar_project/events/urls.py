from django.urls import path
from . import views

urlpatterns = [
    path('calendar/', views.calendar_view, name='calendar_view'),
    path('api/', views.events_api, name='events_api'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
]
