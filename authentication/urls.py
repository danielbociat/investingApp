from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('registerUser/', views.register_user, name='registerUser'),
    path('registerCompany/', views.index, name='registerCompany'),

    path('', views.home, name='home'),
]