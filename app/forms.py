from django import forms
from django.forms import NumberInput, TextInput


class Form(forms.Form):
    fuel_price = forms.FloatField(widget=NumberInput(attrs={'class': 'form-control', 'style': 'font-size: 16px; text-align: center;'}))
    electricity_price = forms.FloatField(widget=NumberInput(attrs={'class': 'form-control', 'style': 'font-size: 16px; text-align: center;'}))
    dvz_maintenance_factor = forms.FloatField(widget=NumberInput(attrs={'class': 'form-control', 'style': 'font-size: 16px; text-align: center;'}))
    ev_maintenance_factor = forms.FloatField(widget=NumberInput(attrs={'class': 'form-control', 'style': 'font-size: 16px; text-align: center;'}))
    dvz_range = forms.FloatField(widget=NumberInput(attrs={'class': 'form-control', 'style': 'font-size: 16px; text-align: center;'}))
    ev_range = forms.FloatField(widget=NumberInput(attrs={'class': 'form-control', 'style': 'font-size: 16px; text-align: center;'}))
    charging_speed = forms.FloatField(widget=NumberInput(attrs={'class': 'form-control', 'style': 'font-size: 16px; text-align: center;'}))
    refueling_speed = forms.FloatField(widget=NumberInput(attrs={'class': 'form-control', 'style': 'font-size: 16px; text-align: center;'}))
    ev_subsidy = forms.FloatField(widget=NumberInput(attrs={'class': 'form-control', 'style': 'font-size: 16px; text-align: center;'}))
    dvz_subsidy = forms.FloatField(widget=NumberInput(attrs={'class': 'form-control', 'style': 'font-size: 16px; text-align: center;'}))
    years = forms.IntegerField(
        label="Years",
        widget=forms.NumberInput(attrs={
            'type': 'range',
            'min': '0',
            'max': '50',
            'step': '1',
            'class': 'form-range'  # Optional for styling
        }), initial=0
    )
