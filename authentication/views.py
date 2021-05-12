from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import RegisterUserForm, RegisterInvestorForm, RegisterCompanyForm
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


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

            login(request, user)
            return redirect('home')
    else:
        formUser = RegisterUserForm(request.POST)
        formInvestor = RegisterInvestorForm(request.POST)
    return render(request, 'authentication/registerUser.html', {'form': formUser, 'form2':formInvestor})


def register_company(request):
    if request.method == 'POST':
        formUser = RegisterUserForm(request.POST)
        formCompany = RegisterCompanyForm(request.POST)

        if formUser.is_valid() and formCompany.is_valid():
            user_toSave = formUser.save()
            company_toSave = formCompany.save(commit=False)

            company_toSave.user = user_toSave
            company_toSave.save()

            email = formUser.cleaned_data.get('email')
            raw_password = formUser.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)

            login(request, user)
            return redirect('home')
    else:
        formUser = RegisterUserForm(request.POST)
        formCompany = RegisterCompanyForm(request.POST)
    return render(request, 'authentication/registerCompany.html', {'form': formUser, 'form2': formCompany})


def login_page(request):
    context = {}

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:8000/')
        else:
            messages.info(request, 'email OR password is incorrect')
            return render(request, 'authentication/login.html', context)

    return render(request, 'authentication/login.html', context)


def home(request):
    context = {}
    template = loader.get_template('authentication/home.html')
    return HttpResponse(template.render(context, request))
