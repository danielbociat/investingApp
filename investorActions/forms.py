from authentication.models import User, Investor, Stock
from django import forms
from django.db import models


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


class AddStock(forms.ModelForm):
    buy_price = forms.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        model = Stock
        fields = ("buy_price", )
