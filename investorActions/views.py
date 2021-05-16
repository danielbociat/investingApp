from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, loader
from .forms import DepositFunds, WithdrawFunds, BuySellStock
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
                obj = Investor.objects.get(user=request.user)
                obj.funds = request.user.investor.funds + amount
                obj.account_value = request.user.investor.account_value + amount
                obj.save()
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
                obj = Investor.objects.get(user=request.user)
                obj.funds=request.user.investor.funds-amount
                obj.account_value=request.user.investor.account_value-amount
                obj.save()
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
        formAcquire = BuySellStock(request.POST)
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

            print(stock.buy_price)

            request.user.investor.funds = request.user.investor.funds - quantity * stock.buy_price
            request.user.investor.save()

            stock.buy_price = float(stock.buy_price) * (1.001) ** float(quantity)
            stock.sell_price = 99 * stock.buy_price / 100
            stock.available_quantity = max_quant - quantity
            stock.save()

            new_val = 0
            for inv in Investor.objects.all():
                new_val = inv.funds
                for aq in AcquiredStock.objects.filter(investors=inv):
                    st = aq.stock
                    new_val = new_val + aq.quantity * st.sell_price
                inv.account_value = new_val
                inv.save()

            return redirect('checkfunds')
        else:
            return redirect('homeinvestor')
    else:
        formAcquire = BuySellStock(request.POST)

    return render(request, template, {'formAcquire':formAcquire})


def sellshares(request):
    template = "investorActions/sellshares.html"
    if request.method == 'POST':
        formAcquire = BuySellStock(request.POST)
        if formAcquire.is_valid():
            quantity = formAcquire.cleaned_data.get('quantity')
            stock = formAcquire.cleaned_data.get('stock')
            acquire_toSave = formAcquire.save(commit=False)
            acquire_toSave.investors = request.user.investor

            if not AcquiredStock.objects.filter(investors=request.user.investor, stock=stock):
                print("Stock not owned")
                return redirect('homeinvestor')
            else:
                obj = AcquiredStock.objects.get(investors=request.user.investor, stock=stock)
                max_quant = obj.quantity
                if quantity > max_quant:
                    print("Quantity too big")
                    return redirect('homeinvestor')
                else:
                    obj.quantity = obj.quantity - quantity
                    if obj.quantity == 0:
                        obj.delete()
                    else:
                        obj.save()

                    request.user.investor.funds = request.user.investor.funds + quantity * stock.sell_price
                    request.user.investor.save()

                    new_val = 0
                    for inv in Investor.objects.all():
                        new_val = inv.funds
                        for aq in AcquiredStock.objects.filter(investors=inv):
                            st = aq.stock
                            new_val = new_val + aq.quantity * st.sell_price
                        inv.account_value = new_val
                        inv.save()

                    stock.buy_price = float(stock.buy_price) * (0.999)**float(quantity)
                    stock.sell_price = 99 * stock.buy_price / 100
                    stock.available_quantity = max_quant + quantity
                    stock.save()

            return redirect('checkfunds')
        else:
            return redirect('homeinvestor')
    else:
        formAcquire = BuySellStock(request.POST)

    return render(request, template, {'formAcquire':formAcquire})