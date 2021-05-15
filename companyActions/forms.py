from authentication.models import User, Investor, Stock, AcquiredStock
from django import forms
from django.db import models
import itertools

class RegisterStock(forms.ModelForm):
    buy_price = forms.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        model = Stock
        fields = ("buy_price", )


class AddStock(forms.ModelForm):
    quantity = forms.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        model = Stock
        fields = ('quantity', )