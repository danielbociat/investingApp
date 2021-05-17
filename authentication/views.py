from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .forms import RegisterUserForm, RegisterInvestorForm, RegisterCompanyForm
from companyActions.forms import RegisterStock
from authentication.models import *
from .decorators import unauthenticated_user
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@unauthenticated_user
def register_investor(request):

    if request.method == 'POST':
        formUser = RegisterUserForm(request.POST)
        formInvestor = RegisterInvestorForm(request.POST)

        if formUser.is_valid() and formInvestor.is_valid():
            user_toSave = formUser.save()
            investor_toSave = formInvestor.save(commit=False)

            investor_toSave.user = user_toSave
            investor_toSave.save()

            email = formUser.cleaned_data.get('email')
            raw_password = formUser.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)

            return redirect('login')
    else:
        formUser = RegisterUserForm(request.POST)
        formInvestor = RegisterInvestorForm(request.POST)
    return render(request, 'authentication/registerUser.html', {'form': formUser, 'form2':formInvestor})


@unauthenticated_user
def register_company(request):
    if request.method == 'POST':
        formUser = RegisterUserForm(request.POST)
        formCompany = RegisterCompanyForm(request.POST)
        formStock = RegisterStock(request.POST)

        if formUser.is_valid() and formCompany.is_valid() and formStock.is_valid():

            user_toSave = formUser.save()
            company_toSave = formCompany.save(commit=False)
            stock_toSave = formStock.save(commit=False)

            company_toSave.user = user_toSave

            stock_toSave.company = company_toSave
            buy_price = formStock.cleaned_data.get('buy_price')
            stock_toSave.sell_price = 99 * buy_price / 100

            company_toSave.save()
            stock_toSave.save()

            email = formUser.cleaned_data.get('email')
            raw_password = formUser.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)

            #login(request, user)
            return redirect('login')
    else:
        formUser = RegisterUserForm(request.POST)
        formCompany = RegisterCompanyForm(request.POST)
        formStock = RegisterStock(request.POST)
    return render(request, 'authentication/registerCompany.html', {'form': formUser, 'form2': formCompany, 'form3': formStock})


@unauthenticated_user
def login_page(request):
    context = {}

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)

            try:
                Investor.objects.get(user=user)
                return redirect('http://127.0.0.1:8000/homeinvestor')
            except:
                print("AAA")
                return redirect('http://127.0.0.1:8000/homecompany')
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'authentication/login.html', context)

    return render(request, 'authentication/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')


@unauthenticated_user
def home(request):
    context = {}
    template = loader.get_template('authentication/home.html')
    return HttpResponse(template.render(context, request))
