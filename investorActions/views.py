from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
# Create your views here.


def homeinvestor(reuqest):
    template = loader.get_template("investorActions/homeinvestor.html")
    return HttpResponse(template.render())

def depositmoney(request):
    template = loader.get_template("investorActions/depositmoney.html")
    return HttpResponse(template.render())

def withdrawmoney(request):
    template = loader.get_template("investorActions/withdrawmoney.html")
    return HttpResponse(template.render())

def checkfunds(request):
    template = loader.get_template("investorActions/checkfunds.html")
    return HttpResponse(template.render())

def buyshares(request):
    template = loader.get_template("investorActions/buyshares.html")
    return HttpResponse(template.render())

def sellshares(request):
    template = loader.get_template("investorActions/sellshares.html")
    return HttpResponse(template.render())