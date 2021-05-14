from authentication.models import User, Investor, Company
from django import forms
from django.db import models


class DepositFunds(forms.Form):
    amount = forms.IntegerField()

    class Meta:
        model = Investor
        fields = ("amount", )


class WithdrawFunds(forms.Form):
    amount = forms.IntegerField()

    class Meta:
        model = Investor
        fields = ("amount", )