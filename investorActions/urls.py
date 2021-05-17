from django.urls import path
from . import views

urlpatterns = [
    path('homeinvestor/', views.homeinvestor, name='homeinvestor'),
    path('depositmoney/', views.depositmoney, name='depositmoney'),
    path('withdrawmoney/', views.withdrawmoney, name='withdrawmoney'),
    path('checkfunds/', views.checkfunds, name='checkfunds'),
    path('buyshares/', views.buyshares, name='buyshares'),
    path('sellshares/', views.sellshares, name='sellshares'),
]