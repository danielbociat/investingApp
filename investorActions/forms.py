from authentication.models import User, Investor, Stock, AcquiredStock
from django import forms
from django.db import models
import itertools

class DepositFunds(forms.Form):
    amount = forms.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        model = Investor
        fields = ("amount", )


class WithdrawFunds(forms.Form):
    amount = forms.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        model = Investor
        fields = ("amount", )


class BuyStock(forms.ModelForm):

    all_stocks = Stock.objects.all()

    try:
        stock = forms.Select(choices=all_stocks)
    except:
        stock = None
    quantity = forms.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        model = AcquiredStock
        fields = ("stock", "quantity")


