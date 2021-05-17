from authentication.models import *
from django import forms


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


class BuySellStock(forms.ModelForm):

    all_stocks = Stock.objects.all()

    try:
        stock = forms.CharField(widget=forms.Select, choices=all_stocks)
    except:
        stock = None
    quantity = forms.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        model = AcquiredStock
        fields = ("stock", "quantity")
