from django.db import models
from django.contrib.auth.models import User
from city.models import City

class Event(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='events')
    name = models.CharField(max_length=200)
    description = models.TextField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=500)
    location_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    tickets_count = models.PositiveIntegerField(default=1)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"