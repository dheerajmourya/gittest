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
from django.utils.translation import gettext_lazy as _

from datetime import timedelta
from django.core.exceptions import ValidationError
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

    # 🔹 Price Validity Based on Dates
    start_date = models.DateField(_("Price Valid From"))
    end_date = models.DateField(_("Price Valid To"))

    # 🔹 Month & Year for Monthly Management
    month = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 13)], blank=True, null=True)  # 1 to 12 (Jan to Dec)
    year = models.PositiveIntegerField(blank=True, null=True)

    # ✅ Hotel Pricing
    STANDARD_ROOM_PRICE = models.PositiveIntegerField(default=0)
    DELUXE_ROOM_PRICE = models.PositiveIntegerField(default=0)
    SUPER_DELUXE_ROOM_PRICE = models.PositiveIntegerField(default=0)

    STANDARD_EXTRA_BED_PRICE = models.PositiveIntegerField(default=0)
    DELUXE_EXTRA_BED_PRICE = models.PositiveIntegerField(default=0)
    SUPER_DELUXE_EXTRA_BED_PRICE = models.PositiveIntegerField(default=0)

    # ✅ Transport Pricing
    SEDAN_PRICE = models.PositiveIntegerField(default=0)
    SUV_PRICE = models.PositiveIntegerField(default=0)
    TEMPO_14_PRICE = models.PositiveIntegerField(default=0)
    TEMPO_17_PRICE = models.PositiveIntegerField(default=0)

    # ✅ Volvo Pricing
    VOLVO_1_SIDE_PRICE = models.PositiveIntegerField(default=0)
    VOLVO_BOTH_SIDE_PRICE = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Destination Price"
        verbose_name_plural = "Destination Prices"
        unique_together = ('trip_place', 'month', 'year')  # ✅ Ensures unique pricing per month

    def __str__(self):
        return f"{self.trip_place} - {self.start_date.strftime('%d-%b-%Y')} to {self.end_date.strftime('%d-%b-%Y')}"
    

    # def __str__(self):
    #     return f"{self.trip_place} ({self.start_date} - {self.end_date})"

    def clean(self):
        """
        ✅ **1. Start Date हमेशा End Date से पहले या बराबर हो**
        ✅ **2. Same `trip_place` के लिए Overlapping Date Range Allow न हो**
        """
        if self.start_date > self.end_date:
            raise ValidationError(_("Start date cannot be greater than end date."))

        overlapping_entries = TripPlacePricing.objects.filter(
            trip_place=self.trip_place,
            start_date__lte=self.end_date,
            end_date__gte=self.start_date
        )

        if self.pk:
            overlapping_entries = overlapping_entries.exclude(pk=self.pk)

        if overlapping_entries.exists():
            raise ValidationError(_("A pricing entry already exists for this trip place in the selected date range."))

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)