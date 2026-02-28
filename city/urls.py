from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('city/<int:city_id>/events/', views.city_events, name='city_events'),
]