from .models import Booking, Flight
from rest_framework.generics import ListAPIView
from .serializers import FlightListSerializer, BookingListSerializer
from django.utils import timezone


class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer


class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gt=timezone.now())
    serializer_class = BookingListSerializer
