from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, loader

from authentication.models import Stock, Company, User
from companyActions.forms import AddStock

# Create your views here.

def homecompany(request):
    template = loader.get_template("companyActions/homecompany.html")
    return HttpResponse(template.render())

def addshares(request):
    template = "companyActions/addshares.html"
    if request.method == "POST":
        AddStockForm = AddStock(request.POST)

        if AddStockForm.is_valid():
            quantity = AddStockForm.cleaned_data.get("quantity")
            if quantity >= 0:
                obj = Stock.objects.get(company=request.user.company)
                obj.available_quantity = obj.available_quantity + quantity
                obj.save()

        return redirect('homecompany')
    else:
        AddStockForm = AddStock(request.POST)

    return render(request, template, {'formAddStock': AddStockForm})




    return HttpResponse(template.render())

def removeshares(request):
    template = "companyActions/removeshares.html"
    return render(request, template)

def info(request):
    template = "companyActions/info.html"
    return render(request, template)