from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('registerUser/', views.register_investor, name='registerUser'),
    path('registerCompany/', views.register_company, name='registerCompany'),

    path('', views.home, name='home'),
]