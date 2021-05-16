from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, loader

from authentication.models import Stock, Company, User
from companyActions.forms import AddRemoveStock
from django.contrib.auth.decorators import login_required
from authentication.decorators import allowed_users, unauthenticated_user
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

        return redirect('homecompany')
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
            else:
                print("Wrong quantity")

        return redirect('homecompany')
    else:
        RemoveStockForm = AddRemoveStock(request.POST)

    return render(request, template, {'formRemoveStock': RemoveStockForm})
