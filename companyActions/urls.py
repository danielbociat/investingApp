from django.urls import path
from . import views
from authentication import views as aut

urlpatterns = [
    path('homecompany/', views.homecompany, name='homecompany'),
    path('addshares/', views.addshares, name='addshares'),
    path('removeshares/', views.removeshares, name='removeshares'),
    path('info/', views.info, name='info'),
]