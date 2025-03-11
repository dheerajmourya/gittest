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



def calculate_cost(no_of_pax, no_of_stays, hotel_category, no_of_rooms, extra_bed, transport_type, volvo_type, profit_percentage):
    # **✅ Stay Cost Calculation (Matching Excel Formula)**
    hotel_category = hotel_category.lower()

    if hotel_category == "standard":
        hotel_cost = (no_of_rooms * no_of_stays * 2000) + (extra_bed * no_of_stays * 800)
    elif hotel_category == "deluxe":
        hotel_cost = (no_of_rooms * no_of_stays * 3000) + (extra_bed * no_of_stays * 1000)
    elif hotel_category == "super deluxe":
        hotel_cost = (no_of_rooms * no_of_stays * 4500) + (extra_bed * no_of_stays * 1500)
    else:
        hotel_cost = 0  

    # **✅ Transport Cost Calculation (Fixed)**
    transport_rates = {'SEDAN': 3500, 'SUV': 5500, 'TEMPO 14': 6500, 'TEMPO 17': 7000}
    transport_cost = (no_of_pax + 1) * transport_rates.get(transport_type.upper(), 0)

    # **✅ Volvo Cost Calculation**
    volvo_rates = {'1 SIDE': 1000, 'BOTH SIDE': 2000}
    volvo_cost = no_of_pax * volvo_rates.get(volvo_type.upper(), 0)

    # **✅ Operational Cost Calculation**
    operational_cost = hotel_cost + transport_cost + volvo_cost

    # **✅ Profit Percentage Calculation (Dropdown से लिया गया %)**
    profit_percentage_value = float(profit_percentage.strip('%')) / 100  # Convert "20%" to 0.2
    profit_amount = operational_cost * profit_percentage_value

    # **✅ Final Package Cost**
    final_package_cost = operational_cost + profit_amount

    return {
        'stay_cost': hotel_cost,
        'transport_cost': transport_cost,
        'volvo_cost': volvo_cost,
        'operational_cost': operational_cost,
        'profit_amount': profit_amount,
        'final_package_cost': final_package_cost
    }


from django.shortcuts import render
from .forms import CostCalculatorForm


def cost_calculator_view(request):
    # Initialize variables
    hotel_cost = transport_cost = volvo_cost = operational_cost = total_cost = profit_amount = final_package_cost = None

    if request.method == 'POST':
        form = CostCalculatorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Debugging Prints
            print(f"Form Data: {data}")

            # ✅ Calling the updated `calculate_cost` function
            cost_details = calculate_cost(
                data['no_of_pax'], 
                data['no_of_stays'], 
                data['hotel_category'], 
                data['no_of_rooms'], 
                data.get('extra_bed', 0) or 0,  # Handle None case
                data['transport_type'], 
                data['volvo_type'],
                data['profit_percentage']  # No more `operational_cost`
            )

            # ✅ Assigning the calculated values
            hotel_cost = cost_details['stay_cost']
            transport_cost = cost_details['transport_cost']
            volvo_cost = cost_details['volvo_cost']
            operational_cost = cost_details['operational_cost']  # Calculated inside function
            profit_amount = cost_details['profit_amount']
            final_package_cost = cost_details['final_package_cost']

    else:
        form = CostCalculatorForm()

    return render(request, 'templates/calculator.html', {
        'form': form,
        'hotel_cost': hotel_cost,
        'transport_cost': transport_cost,
        'volvo_cost': volvo_cost,
        'operational_cost': operational_cost,
        'profit_amount': profit_amount,
        'final_package_cost': final_package_cost
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

