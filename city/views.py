from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import City
from events.models import Event 
from django.contrib.auth import login


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def home(request):
    cities = City.objects.all()
    return render(request, 'home.html', {'cities': cities})


def city_events(request, city_id):
    city = get_object_or_404(City, id=city_id)
    events = Event.objects.filter(city=city, is_active=True)
    return render(request, 'events/event_list.html', {'city': city, 'events': events})