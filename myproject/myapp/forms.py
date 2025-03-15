from django import forms
from .models import TripPlace
from django.core.validators import MaxValueValidator

class CostCalculatorForm(forms.Form):
    trip_place = forms.ModelChoiceField(queryset=TripPlace.objects.all(), label="Destinations")
    travel_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Travel Date")
    no_of_pax = forms.IntegerField(
        label="Number of People",
        validators=[MaxValueValidator(999)],
        widget=forms.NumberInput(attrs={'min': 1, 'max': 999, 'oninput': "limitDigits(this, 3)"})
    )
    
    no_of_stays = forms.IntegerField(
        label="Number of Stays",
        validators=[MaxValueValidator(999)],
        widget=forms.NumberInput(attrs={'min': 1, 'max': 999, 'oninput': "limitDigits(this, 3)"})
    )
    
    no_of_rooms = forms.IntegerField(
        label="Number of Rooms",
        validators=[MaxValueValidator(999)],
        widget=forms.NumberInput(attrs={'min': 1, 'max': 999, 'oninput': "limitDigits(this, 3)"})
    )
    
    extra_bed = forms.IntegerField(
        label="Extra Beds",
        required=False,
        initial=0,
        validators=[MaxValueValidator(999)],
        widget=forms.NumberInput(attrs={'min': 0, 'max': 999, 'oninput': "limitDigits(this, 3)"})
    )

    hotel_category = forms.ChoiceField(
        choices=[('STANDARD', 'Standard'), ('DELUXE', 'Deluxe'), ('SUPER DELUXE', 'Super Deluxe')],
        label="Hotel Category"
    )

    transport_type = forms.ChoiceField(
        choices=[('SEDAN', 'Sedan'), ('SUV', 'SUV'), ('TEMPO 14', 'Tempo 14'), ('TEMPO 17', 'Tempo 17')],
        label="Transport Type"
    )

    volvo_type = forms.ChoiceField(
        choices=[('1 SIDE', 'One Side'), ('BOTH SIDE', 'Both Side')],
        label="Volvo Type",
        required=False
    )

    profit_percentage = forms.ChoiceField(
        choices=[('20%', '20%'), ('25%', '25%'), ('30%', '30%'), ('35%', '35%'), ('40%', '40%')],
        label="Profit Percentage"
    )