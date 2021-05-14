from django.http import HttpResponse
from django.shortcuts import redirect
from authentication.models import Investor, Company, User


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.is_staff:
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

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("you are not authorized")
        return wrapper_func
    return decorator