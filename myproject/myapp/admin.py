from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import HotelPrice, TransportPrice, TripPlace, TripPlacePricing, VolvoPrice

# @admin.register(HotelPrice)
# class HotelPriceAdmin(admin.ModelAdmin):
#     list_display = ('category', 'room_price', 'extra_bed_price')

# @admin.register(TransportPrice)
# class TransportPriceAdmin(admin.ModelAdmin):
#     list_display = ('transport_type', 'price_per_day')

# @admin.register(VolvoPrice)
# class VolvoPriceAdmin(admin.ModelAdmin):
#     list_display = ('volvo_type', 'price_per_pax')

@admin.register(TripPlace)
class TripPlaceAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(TripPlacePricing)
class TripPlacePricingAdmin(admin.ModelAdmin):
    list_display = ('trip_place',)
    list_filter = ('trip_place',)
