from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
# Create your views here.


def homeinvestor(request):
    template = "investorActions/homeinvestor.html"
    return render(request, template)


def depositmoney(request):
    template = "investorActions/depositmoney.html"
    return render(request, template)


def withdrawmoney(request):
    template = "investorActions/withdrawmoney.html"
    return render(request, template)


def checkfunds(request):
    template = "investorActions/checkfunds.html"
    return render(request, template)


def buyshares(request):
    template = "investorActions/buyshares.html"
    return render(request, template)


def sellshares(request):
    template = "investorActions/sellshares.html"
    return render(request, template)
