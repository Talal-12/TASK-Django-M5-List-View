"""airport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from flights.views import FlightListView, BookingListView, BookingDetailView, BookingUpdateView, BookingDeleteView, BookingCreateView

from users.views import RegisterView, LoginView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("flights/", FlightListView.as_view(), name="flights_list"),
    path("bookings/", BookingListView.as_view(), name="bookings_list"),
    path("bookings/<int:booking_id>/",
         BookingDetailView.as_view(), name="bookings_detail"),
    path("bookings/update/<int:booking_id>/",
         BookingUpdateView.as_view(), name="bookings_update"),
    path("bookings/cancel/<int:booking_id>/",
         BookingDeleteView.as_view(), name="bookings_cancel"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("book/<int:flight_id/", BookingCreateView.as_view(), name="book_flight")
]
