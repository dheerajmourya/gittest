from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
@login_required
def home(request):
    print("hello")
    user = request.user  # लॉगिन किया हुआ यूजर
    context = {
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }
    print("############################",context)
    return render(request,'templates/newtest.html', context,)



from .models import HotelPrice, TransportPrice, TripPlacePricing, VolvoPrice

from .models import TripPlacePricing

from datetime import datetime
from .models import TripPlacePricing

def calculate_cost(trip_place, travel_date, no_of_pax, no_of_stays, hotel_category, no_of_rooms, extra_bed, transport_type, volvo_type, profit_percentage):
    # ✅ Travel Date से Pricing Fetch करें
    try:
        pricing = TripPlacePricing.objects.get(
            trip_place=trip_place,
            start_date__lte=travel_date,
            end_date__gte=travel_date
        )
    except TripPlacePricing.DoesNotExist:
        return {'error':  f"No package available for {travel_date.strftime('%d-%b-%Y')}"}

    # ✅ **Hotel Cost Calculation**
    hotel_prices = {
        "STANDARD": (pricing.STANDARD_ROOM_PRICE, pricing.STANDARD_EXTRA_BED_PRICE),
        "DELUXE": (pricing.DELUXE_ROOM_PRICE, pricing.DELUXE_EXTRA_BED_PRICE),
        "SUPER DELUXE": (pricing.SUPER_DELUXE_ROOM_PRICE, pricing.SUPER_DELUXE_EXTRA_BED_PRICE),
    }
    room_price, extra_bed_price = hotel_prices.get(hotel_category.upper(), (0, 0))
    hotel_cost = (no_of_rooms * no_of_stays * room_price) + (extra_bed * no_of_stays * extra_bed_price)

    # ✅ **Transport Cost Calculation**
    transport_rates = {
        'SEDAN': pricing.SEDAN_PRICE, 'SUV': pricing.SUV_PRICE,
        'TEMPO 14': pricing.TEMPO_14_PRICE, 'TEMPO 17': pricing.TEMPO_17_PRICE
    }
    transport_cost = (no_of_stays + 1) * transport_rates.get(transport_type.upper(), 0)

    # ✅ **Volvo Cost Calculation**
    volvo_rates = {
        '1 SIDE': pricing.VOLVO_1_SIDE_PRICE, 'BOTH SIDE': pricing.VOLVO_BOTH_SIDE_PRICE
    }
    volvo_cost = no_of_pax * volvo_rates.get(volvo_type.upper(), 0)

    # ✅ **Operational Cost**
    operational_cost = hotel_cost + transport_cost + volvo_cost

    # ✅ **Profit Calculation**
    profit_percentage_value = float(profit_percentage.strip('%')) / 100
    profit_amount = operational_cost * profit_percentage_value

    # ✅ **Final Package Cost**
    final_package_cost = operational_cost + profit_amount

    return {
        'stay_cost': hotel_cost, 'transport_cost': transport_cost,
        'volvo_cost': volvo_cost, 'operational_cost': operational_cost,
        'profit_amount': profit_amount, 'final_package_cost': final_package_cost
    }


from django.shortcuts import render
from .forms import CostCalculatorForm
from .models import TripPlace

def cost_calculator_view(request):
    hotel_cost = transport_cost = volvo_cost = operational_cost = profit_amount = final_package_cost = None
    error_message = None  # 🔹 Store Error Message

    if request.method == 'POST':
        form = CostCalculatorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            trip_place = data['trip_place']
            travel_date = data['travel_date']  # ✅ **Date from Form**

            # ✅ **Calling the Updated Cost Calculation Function**
            cost_details = calculate_cost(
                trip_place, travel_date, data['no_of_pax'], data['no_of_stays'],
                data['hotel_category'], data['no_of_rooms'], data.get('extra_bed', 0) or 0,
                data['transport_type'], data['volvo_type'], data['profit_percentage']
            )

            # ✅ **Check if Error Message is Present**
            if 'error' in cost_details:
                error_message = cost_details['error']
                print("hrhrhrrhrhhrrhhrhrhr",error_message)
            else:
                # ✅ **Assigning Values**
                hotel_cost = cost_details['stay_cost']
                transport_cost = cost_details['transport_cost']
                volvo_cost = cost_details['volvo_cost']
                operational_cost = cost_details['operational_cost']
                profit_amount = cost_details['profit_amount']
                final_package_cost = cost_details['final_package_cost']
    else:
        form = CostCalculatorForm()

    return render(request, 'templates/calculator.html', {
        'form': form, 'hotel_cost': hotel_cost, 'transport_cost': transport_cost,
        'volvo_cost': volvo_cost, 'operational_cost': operational_cost,
        'profit_amount': profit_amount, 'final_package_cost': final_package_cost,
        'error_message': error_message  # ✅ Pass Error Message to Template
    })






# VIDEO CALLING APP

import time
import random
from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder

# Agora के क्रेडेंशियल्स
APP_ID = "fb139cb7dee74d688969f813d052ae80"
APP_CERTIFICATE = "fcdc293d55e14120898c4de971df1cf6"

def generate_agora_token(request, channel_name):
    uid = random.randint(1, 1000)  # Unique User ID
    role = 1  # Broadcaster Role
    expiration_time = 3600  # Token Expiry (1 hour)

    current_time = int(time.time())
    privilege_expired_ts = current_time + expiration_time

    # Token Generate करें
    token = RtcTokenBuilder.buildTokenWithUid(
        APP_ID, APP_CERTIFICATE, channel_name, uid, role, privilege_expired_ts
    )

    return JsonResponse({'token': token, 'uid': uid, 'channel_name': channel_name})


def video_call(request):
    return render(request, "templates/index.html")

