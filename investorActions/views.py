from django.shortcuts import render, redirect
from .forms import DepositFunds, WithdrawFunds, BuySellStock
from authentication.models import *
# Create your views here.
from django.contrib.auth.decorators import login_required
from authentication.decorators import allowed_users
from django.contrib import messages


@login_required(login_url='login')
@allowed_users("investor")
def homeinvestor(request):
    template = "investorActions/homeinvestor.html"
    return render(request, template)


@login_required(login_url='login')
@allowed_users("investor")
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
                try:
                    obj.save()
                except:
                    return redirect("depositmoney")
            else:
                messages.error(request, "Please enter a positive value")
                return redirect('depositmoney')
            return redirect('checkfunds')
        else:
            messages.error(request, "Please enter a valid amount")
            return redirect("depositmoney")
    else:
        formAmount = DepositFunds(request.POST)

    return render(request, template, {'formAmount':formAmount})


@login_required(login_url='login')
@allowed_users("investor")
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
                try:
                    obj.save()
                except:
                    return redirect("withdrawmoney")
            elif  amount < 0:
                messages.error(request, 'Please enter a positive value')
                return redirect('withdrawmoney')
            elif amount > request.user.investor.funds:
                messages.error(request, 'Insufficient funds')
                return redirect('withdrawmoney')
            return redirect('checkfunds')

        else:
            messages.error(request, 'Please enter a valid amount')
            return redirect("withdrawmoney")
    else:
        formAmount = WithdrawFunds()

    return render(request, template, {'formAmount':formAmount})


@login_required(login_url='login')
@allowed_users("investor")
def checkfunds(request):
    template = "investorActions/checkfunds.html"
    return render(request, template)


@login_required(login_url='login')
@allowed_users("investor")
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
                messages.error(request, 'Not enough shares available')
                return redirect('buyshares')

            if quantity * stock.buy_price > request.user.investor.funds:
                messages.error(request, 'Insufficient funds')
                return redirect('buyshares')

            if not AcquiredStock.objects.filter(investors=request.user.investor, stock=stock):
                acquire_toSave.save()
            else:
                obj = AcquiredStock.objects.get(investors=request.user.investor, stock=stock)
                obj.quantity = obj.quantity + quantity
                obj.save()

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
                    if aq.investors == inv:
                        new_val = new_val + aq.quantity * st.sell_price
                inv.account_value = new_val
                inv.save()

            return redirect('checkfunds')
        else:
            messages.error(request, "Invalid")
            return redirect('sellshares')
    else:
        formAcquire = BuySellStock(request.POST)

    return render(request, template, {'formAcquire': formAcquire})


@login_required(login_url='login')
@allowed_users("investor")
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
                messages.error(request, "Share not owned")
                return redirect('sellshares')
            else:
                obj = AcquiredStock.objects.get(investors=request.user.investor, stock=stock)
                max_quant = obj.quantity
                if quantity > max_quant:
                    messages.error(request, "Insufficient shares")
                    return redirect('sellshares')
                elif quantity < 0:
                    messages.error(request, "Please enter a positive value")
                    return redirect('sellshares')
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
                            if aq.investors == inv:
                                new_val = new_val + aq.quantity * st.sell_price
                        inv.account_value = new_val
                        inv.save()

                    stock.buy_price = float(stock.buy_price) * (0.999)**float(quantity)
                    stock.sell_price = 99 * stock.buy_price / 100
                    stock.available_quantity = max_quant + quantity

                    stock.save()

            return redirect('checkfunds')
        else:
            messages.error(request, "Invalid")
            return redirect('sellshares')
    else:
        formAcquire = BuySellStock(request.POST)

    return render(request, template, {'formAcquire':formAcquire})