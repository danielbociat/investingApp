from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, loader
from .forms import DepositFunds, WithdrawFunds, BuyStock
from authentication.models import Investor, Stock, Company, AcquiredStock
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
            if amount >= 0:
                Investor.objects.filter(user=request.user).update(funds=amount+request.user.investor.funds)
            return redirect('homeinvestor')
        else:
            return redirect("depositmoney")
    else:
        formAmount = DepositFunds(request.POST)

    return render(request, template, {'formAmount':formAmount})


def withdrawmoney(request):
    template = "investorActions/withdrawmoney.html"
    if request.method == 'POST':
        formAmount = WithdrawFunds(request.POST)
        if formAmount.is_valid():
            amount = formAmount.cleaned_data.get("amount")
            if 0 <= amount <= request.user.investor.funds:
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
    if request.method == 'POST':
        formAcquire = BuyStock(request.POST)
        if formAcquire.is_valid():
            quantity = formAcquire.cleaned_data.get('quantity')
            stock = formAcquire.cleaned_data.get('stock')
            acquire_toSave = formAcquire.save(commit=False)
            acquire_toSave.investors = request.user.investor


            max_quant = stock.available_quantity

            if quantity > max_quant:
                print("Quantity too big")
                return redirect('homeinvestor')

            if quantity * stock.buy_price > request.user.investor.funds:
                print("Insufficient funds")
                return redirect('homeinvestor')

            if not AcquiredStock.objects.filter(investors=request.user.investor, stock=stock):
                acquire_toSave.save()
            else:
                obj = AcquiredStock.objects.get(investors=request.user.investor, stock=stock)
                obj.quantity = obj.quantity + quantity
                obj.save()

            request.user.investor.funds = request.user.investor.funds - quantity * stock.buy_price
            request.user.investor.save()

            stock.available_quantity = max_quant - quantity
            stock.save()

            return redirect('checkfunds')
        else:
            return redirect('homeinvestor')
    else:
        formAcquire = BuyStock(request.POST)

    return render(request, template, {'formAcquire':formAcquire})


def sellshares(request):
    template = "investorActions/sellshares.html"
    return render(request, template)
