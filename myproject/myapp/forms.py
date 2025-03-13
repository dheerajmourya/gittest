from django import forms

from .models import TripPlace

class CostCalculatorForm(forms.Form):
    trip_place = forms.ModelChoiceField(queryset=TripPlace.objects.all(), label="Trip Place")
    no_of_pax = forms.IntegerField(label="Number of People")
    no_of_stays = forms.IntegerField(label="Number of Stays")
    no_of_rooms = forms.IntegerField(label="Number of Rooms")
    extra_bed = forms.IntegerField(label="Extra Beds", required=False, initial=0)

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

