from .models import Booking, Flight
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import FlightListSerializer, BookingListSerializer, BookingDetailSerializer
from django.utils import timezone


class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer


class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gt=timezone.now())
    serializer_class = BookingListSerializer


class BookingDetailView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer
    lookup_field = "id"
    lookup_url_kwarg = "article_id"
