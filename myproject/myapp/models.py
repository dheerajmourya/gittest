from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# ...................................................................

# ✅ Hotel Price Model
class HotelPrice(models.Model):
    CATEGORY_CHOICES = [
        ('STANDARD', 'Standard'),
        ('DELUXE', 'Deluxe'),
        ('SUPER DELUXE', 'Super Deluxe'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, unique=True)
    room_price = models.PositiveIntegerField()
    extra_bed_price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.category} - ₹{self.room_price}/room, ₹{self.extra_bed_price}/extra bed"

# ✅ Transport Price Model
class TransportPrice(models.Model):
    TRANSPORT_CHOICES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('TEMPO 14', 'Tempo 14'),
        ('TEMPO 17', 'Tempo 17'),
    ]
    transport_type = models.CharField(max_length=20, choices=TRANSPORT_CHOICES, unique=True)
    price_per_day = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.transport_type} - ₹{self.price_per_day}/day"

# ✅ Volvo Price Model
class VolvoPrice(models.Model):
    VOLVO_CHOICES = [
        ('1 SIDE', 'One Side'),
        ('BOTH SIDE', 'Both Side'),
    ]
    volvo_type = models.CharField(max_length=20, choices=VOLVO_CHOICES, unique=True)
    price_per_pax = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.volvo_type} - ₹{self.price_per_pax}/pax"
    



# .....................................................................
    
from django.db import models

class TripPlace(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Destination"
        verbose_name_plural = "Destinations"

    def __str__(self):
        return self.name

# ✅ Single Model for Pricing (Hotel, Transport, Volvo)
class TripPlacePricing(models.Model):
    trip_place = models.ForeignKey(TripPlace, on_delete=models.CASCADE)

    # Hotel Pricing
    STANDARD_ROOM_PRICE = models.PositiveIntegerField(default=0)
    DELUXE_ROOM_PRICE = models.PositiveIntegerField(default=0)
    SUPER_DELUXE_ROOM_PRICE = models.PositiveIntegerField(default=0)
    
    STANDARD_EXTRA_BED_PRICE = models.PositiveIntegerField(default=0)
    DELUXE_EXTRA_BED_PRICE = models.PositiveIntegerField(default=0)
    SUPER_DELUXE_EXTRA_BED_PRICE = models.PositiveIntegerField(default=0)

    # Transport Pricing
    SEDAN_PRICE = models.PositiveIntegerField(default=0)
    SUV_PRICE = models.PositiveIntegerField(default=0)
    TEMPO_14_PRICE = models.PositiveIntegerField(default=0)
    TEMPO_17_PRICE = models.PositiveIntegerField(default=0)

    # Volvo Pricing
    VOLVO_1_SIDE_PRICE = models.PositiveIntegerField(default=0)
    VOLVO_BOTH_SIDE_PRICE = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Destination Price"
        verbose_name_plural = "Destination Price"

    def __str__(self):
        return f"{self.trip_place} Pricing"

