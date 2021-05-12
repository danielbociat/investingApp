from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authentication.models import Investor, Company, User

# Register your models here.


class Admin(UserAdmin):
    list_display = ('email', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'is_admin')
    readonly_fields = ('id', 'date_joined', 'last_login')

    ordering = ('email', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User)
admin.site.register(Investor)
admin.site.register(Company)


