from .models import Booking, Flight
from rest_framework.generics import ListAPIView
from .serializers import FlightListSerializer, BookingListSerializer


class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer


class BookingListView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer
