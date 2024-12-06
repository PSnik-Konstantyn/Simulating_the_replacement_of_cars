import json

from django.shortcuts import render
from django.http import JsonResponse
from .forms import Form
from .model.Calculations import calculate_transition_matrix
from .model.ModelMain import initial_ev_share, initial_dvz_share, simulate_changing


def calc(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            fuel_price = form.cleaned_data['fuel_price']
            fuel_price_trend = form.cleaned_data['fuel_price_trend']
            fuel_price_trend_way = request.POST.get('fuel_price_trend_way')

            electricity_price = form.cleaned_data['electricity_price']
            electricity_price_trend = form.cleaned_data['electricity_price_trend']
            electricity_price_trend_way = request.POST.get('electricity_price_trend_way')

            dvz_maintenance_factor = form.cleaned_data['dvz_maintenance_factor']
            dvz_maintenance_factor_trend = form.cleaned_data['dvz_maintenance_factor_trend']
            dvz_maintenance_factor_trend_way = request.POST.get('dvz_maintenance_factor_way')

            ev_maintenance_factor = form.cleaned_data['ev_maintenance_factor']
            ev_maintenance_factor_trend = form.cleaned_data['ev_maintenance_factor_trend']
            ev_maintenance_factor_trend_way = request.POST.get('ev_maintenance_factor_trend_way')

            dvz_range = form.cleaned_data['dvz_range']
            dvz_range_trend = form.cleaned_data['dvz_range_trend']
            dvz_range_trend_way = request.POST.get('dvz_range_trend_way')

            ev_range = form.cleaned_data['ev_range']
            ev_range_trend = form.cleaned_data['ev_range_trend']
            ev_range_trend_way = request.POST.get('ev_range_trend_way')

            charging_speed = form.cleaned_data['charging_speed']
            charging_speed_trend = form.cleaned_data['charging_speed_trend']
            charging_speed_trend_way = request.POST.get('charging_speed_trend_way')

            refueling_speed = form.cleaned_data['refueling_speed']
            refueling_speed_trend = form.cleaned_data['refueling_speed_trend']
            refueling_speed_trend_way = request.POST.get('refueling_speed_trend_way')

            ev_subsidy = form.cleaned_data['ev_subsidy']
            ev_subsidy_trend = form.cleaned_data['ev_subsidy_trend']
            ev_subsidy_trend_way = request.POST.get('ev_subsidy_trend_way')

            dvz_subsidy = form.cleaned_data['dvz_subsidy']
            dvz_subsidy_trend = form.cleaned_data['dvz_subsidy_trend']
            dvz_subsidy_trend_way = request.POST.get('dvz_subsidy_trend_way')

            years = form.cleaned_data['years']

            transition_matrix = calculate_transition_matrix(fuel_price, electricity_price, dvz_maintenance_factor,
                                                            ev_maintenance_factor,
                                                            dvz_range, ev_range, charging_speed, refueling_speed,
                                                            ev_subsidy, dvz_subsidy)
            result = simulate_changing(initial_dvz_share, initial_ev_share, years, transition_matrix)

            return JsonResponse({"result": result})
        else:
            # В разі недійсної форми також потрібно повернути відповідь у форматі JSON
            return JsonResponse({"errors": form.errors}, status=400)
    else:
        form = Form()

    return render(request, "app/index.html", {'form': form})


def description(request):
    return render(request, 'app/description.html')


def trends(request):
    return render(request, 'app/trends.html')


def about_dvz(request):
    return render(request, 'app/aboutDVZ.html')


def about_ev(request):
    return render(request, 'app/aboutEV.html')
