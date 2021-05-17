from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from authentication.models import *

from companyActions.forms import AddRemoveStock
from django.contrib.auth.decorators import login_required
from authentication.decorators import allowed_users
from django.contrib import messages
# Create your views here.


@login_required(login_url='login')
@allowed_users("company")
def homecompany(request):
    template = loader.get_template("companyActions/homecompany.html")
    return HttpResponse(template.render())


@login_required(login_url='login')
@allowed_users("company")
def addshares(request):
    template = "companyActions/addshares.html"
    if request.method == "POST":
        AddStockForm = AddRemoveStock(request.POST)

        if AddStockForm.is_valid():
            quantity = AddStockForm.cleaned_data.get("quantity")
            if quantity >= 0:
                obj = Stock.objects.get(company=request.user.company)
                obj.available_quantity = obj.available_quantity + quantity
                obj.save()
            else:
                messages.error(request, "Please enter a positive value")
                return redirect('addshares')
        else:
            messages.error(request, "Please enter a valid amount")
            return redirect('addshares')
        return redirect('info')
    else:
        AddStockForm = AddRemoveStock(request.POST)

    return render(request, template, {'formAddStock': AddStockForm})


@login_required(login_url='login')
@allowed_users("company")
def removeshares(request):
    template = "companyActions/removeshares.html"
    if request.method == "POST":
        RemoveStockForm = AddRemoveStock(request.POST)
        if RemoveStockForm.is_valid():
            quantity = RemoveStockForm.cleaned_data.get("quantity")
            obj = Stock.objects.get(company=request.user.company)
            max_quant = obj.available_quantity
            if quantity >= 0 and quantity <= max_quant:
                obj.available_quantity = obj.available_quantity - quantity
                obj.save()
            elif quantity < 0:
                messages.error(request, "Please enter a positive value")
                return redirect('removeshares')
            elif quantity > max_quant:
                messages.error(request, "Insufficient shares")
                return redirect('removeshares')
        else:
            messages.error(request, "Please enter a valid amount")
            return redirect('removeshares')
        return redirect('info')
    else:
        RemoveStockForm = AddRemoveStock(request.POST)
    return render(request, template, {'formRemoveStock': RemoveStockForm})


@login_required(login_url='login')
@allowed_users("company")
def info(request):
    template = "companyActions/info.html"
    return render(request, template)
