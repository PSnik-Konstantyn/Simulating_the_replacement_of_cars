from django import forms
from django.forms import NumberInput, TextInput


class Form(forms.Form):
    fuel_price = forms.FloatField(
        widget=NumberInput(attrs={'class': 'form-control', 'style': 'font-size: 16px; text-align: center;'}),
    )
    fuel_price_trend = forms.FloatField(
        widget=NumberInput(attrs={'class': 'form-control trend-input', 'style': 'font-size: 16px;'}),
        min_value=0,
        required=False
    )

    electricity_price = forms.FloatField(
        widget=NumberInput(attrs={'class': 'form-control', 'style': 'font-size: 16px; text-align: center;'}),
    )
    electricity_price_trend = forms.FloatField(
        widget=NumberInput(attrs={'class': 'form-control trend-input', 'style': 'font-size: 16px;'}),
        min_value=0,
        required=False
    )

    dvz_maintenance_factor = forms.FloatField(
        widget=NumberInput(attrs={'class': 'form-control', 'style': 'font-size: 16px; text-align: center;'}),
    )
    dvz_maintenance_factor_trend = forms.FloatField(
        widget=NumberInput(attrs={'class': 'form-control trend-input', 'style': 'font-size: 16px;'}),
        min_value=0,
        required=False
    )

    ev_maintenance_factor = forms.FloatField(
        widget=NumberInput(attrs={'class': 'form-control', 'style': 'font-size: 16px; text-align: center;'}),
    )
    ev_maintenance_factor_trend = forms.FloatField(
        widget=NumberInput(attrs={'class': 'form-control trend-input', 'style': 'font-size: 16px;'}),
        min_value=0,
        required=False
    )

    dvz_range = forms.FloatField(
        widget=NumberInput(attrs={'class': 'form-control', 'style': 'font-size: 16px; text-align: center;'}),
    )
    dvz_range_trend = forms.FloatField(
        widget=NumberInput(attrs={'class': 'form-control trend-input', 'style': 'font-size: 16px;'}),
        min_value=0,
        required=False
    )

    ev_range = forms.FloatField(
        widget=NumberInput(attrs={'class': 'form-control', 'style': 'font-size: 16px; text-align: center;'}),
    )
    ev_range_trend = forms.FloatField(
        widget=NumberInput(attrs={'class': 'form-control trend-input', 'style': 'font-size: 16px;'}),
        min_value=0,
        required=False
    )

    charging_speed = forms.FloatField(
        widget=NumberInput(attrs={'class': 'form-control', 'style': 'font-size: 16px; text-align: center;'}),
    )
    charging_speed_trend = forms.FloatField(
        widget=NumberInput(attrs={'class': 'form-control trend-input', 'style': 'font-size: 16px;'}),
        min_value=0,
        required=False
    )

    refueling_speed = forms.FloatField(
        widget=NumberInput(attrs={'class': 'form-control', 'style': 'font-size: 16px; text-align: center;'}),
    )
    refueling_speed_trend = forms.FloatField(
        widget=NumberInput(attrs={'class': 'form-control trend-input', 'style': 'font-size: 16px;'}),
        min_value=0,
        required=False
    )

    ev_subsidy = forms.FloatField(
        widget=NumberInput(attrs={'class': 'form-control', 'style': 'font-size: 16px; text-align: center;'}),
    )
    ev_subsidy_trend = forms.FloatField(
        widget=NumberInput(attrs={'class': 'form-control trend-input', 'style': 'font-size: 16px;'}),
        min_value=0,
        required=False
    )

    dvz_subsidy = forms.FloatField(
        widget=NumberInput(attrs={'class': 'form-control', 'style': 'font-size: 16px; text-align: center;'}),
    )
    dvz_subsidy_trend = forms.FloatField(
        widget=NumberInput(attrs={'class': 'form-control trend-input', 'style': 'font-size: 16px;'}),
        min_value=0,
        required=False
    )

    years = forms.IntegerField(
        label="Years",
        widget=forms.NumberInput(attrs={
            'type': 'range',
            'min': '1',
            'max': '50',
            'step': '1',
            'class': 'form-range'  # Optional for styling
        }), initial=1
    )
