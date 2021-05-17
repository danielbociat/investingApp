from django.shortcuts import redirect
from authentication.models import *


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                obj = Investor.objects.get(user=request.user)
                return redirect('http://127.0.0.1:8000/homeinvestor')
            except:
                return redirect('http://127.0.0.1:8000/homecompany')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            usr = request.user

            if Investor.objects.filter(user=usr)  and "investor" not in allowed_roles:
                return redirect('http://127.0.0.1:8000/homeinvestor')

            if Company.objects.filter(user=usr) and "company" not in allowed_roles:
                return redirect('http://127.0.0.1:8000/homecompany')
            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator