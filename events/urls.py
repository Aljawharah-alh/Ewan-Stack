from django.urls import path
from . import views

urlpatterns = [
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('<int:event_id>/book/', views.book_event, name='book_event'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
]