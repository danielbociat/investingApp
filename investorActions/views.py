from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, loader
from .forms import DepositFunds, WithdrawFunds
from authentication.models import Investor
# Create your views here.


def homeinvestor(request):
    template = "investorActions/homeinvestor.html"
    return render(request, template)


def depositmoney(request):
    template = "investorActions/depositmoney.html"
    if request.method == 'POST':
        formAmount = DepositFunds(request.POST)
        if formAmount.is_valid():
            amount = formAmount.cleaned_data.get("amount")
            Investor.objects.filter(user=request.user).update(funds=amount+request.user.investor.funds)
            return redirect('homeinvestor')
        else:
            return redirect("depositmoney")
    else:
        formAmount = DepositFunds()

    return render(request, template, {'formAmount':formAmount})


def withdrawmoney(request):
    template = "investorActions/withdrawmoney.html"
    if request.method == 'POST':
        formAmount = WithdrawFunds(request.POST)
        if formAmount.is_valid():
            amount = formAmount.cleaned_data.get("amount")
            if amount <= request.user.investor.funds:
                Investor.objects.filter(user=request.user).update(funds=request.user.investor.funds-amount)
            return redirect('homeinvestor')
        else:
            return redirect("withdrawmoney")
    else:
        formAmount = WithdrawFunds()

    return render(request, template, {'formAmount':formAmount})


def checkfunds(request):
    template = "investorActions/checkfunds.html"
    return render(request, template)


def buyshares(request):
    template = "investorActions/buyshares.html"
    return render(request, template)


def sellshares(request):
    template = "investorActions/sellshares.html"
    return render(request, template)
