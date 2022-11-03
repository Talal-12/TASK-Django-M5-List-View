from .models import Booking, Flight
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from .serializers import FlightListSerializer, BookingListSerializer, BookingDetailSerializer, BookingUpdateSerializer
from django.utils import timezone
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated


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
    lookup_url_kwarg = "booking_id"


class BookingUpdateView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingUpdateSerializer
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"


class BookingDeleteView(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"


class BookingCreateView(CreateAPIView):
    serializer_class = BookingUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"

    def perform_create(self, serializer):
        serializer.save(user=self.request.user,
                        flight_id=self.kwargs["flight_id"])
