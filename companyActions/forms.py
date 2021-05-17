from authentication.models import *
from django import forms


class RegisterStock(forms.ModelForm):
    buy_price = forms.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        model = Stock
        fields = ("buy_price", )


class AddRemoveStock(forms.ModelForm):
    quantity = forms.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        model = Stock
        fields = ('quantity', )