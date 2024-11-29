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
            electricity_price = form.cleaned_data['electricity_price']
            dvz_maintenance_factor = form.cleaned_data['dvz_maintenance_factor']
            ev_maintenance_factor = form.cleaned_data['ev_maintenance_factor']
            dvz_range = form.cleaned_data['dvz_range']
            ev_range = form.cleaned_data['ev_range']
            charging_speed = form.cleaned_data['charging_speed']
            refueling_speed = form.cleaned_data['refueling_speed']
            ev_subsidy = form.cleaned_data['ev_subsidy']
            dvz_subsidy = form.cleaned_data['dvz_subsidy']
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
