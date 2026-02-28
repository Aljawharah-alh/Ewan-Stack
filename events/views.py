from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event, Booking

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})


@login_required
def book_event(request, event_id):
    if request.method == 'POST':
        event = get_object_or_404(Event, id=event_id)
        count = request.POST.get('tickets_count', 1)
        Booking.objects.create(user=request.user, event=event, tickets_count=count)
        return redirect('my_bookings')


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'events/my_bookings.html', {'bookings': bookings})
