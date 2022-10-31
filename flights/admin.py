from django.contrib import admin
from flights.models import Booking, Flight

# Register your models here.
admin.site.register([Flight, Booking])
