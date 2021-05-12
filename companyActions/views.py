from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
# Create your views here.

def homecompany(request):
    template = loader.get_template("companyActions/homecompany.html")
    return HttpResponse(template.render())

def addshares(reuqest):
    template = loader.get_template("companyActions/addshares.html")
    return HttpResponse(template.render())

def removeshares(request):
    template = loader.get_template("companyActions/removeshares.html")
    return HttpResponse(template.render())
