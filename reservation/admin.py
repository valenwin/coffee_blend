from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone',
                    'date', 'time')
    list_filter = ('date', 'time')
    search_fields = ('first_name', 'last_name', 'phone')
    list_per_page = 20
