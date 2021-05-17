from django.contrib import admin
from authentication.models import *

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('email',  'is_admin', 'is_staff')
    search_fields = ('email', 'is_admin')
    readonly_fields = ('id',)
    ordering = ('email',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class InvestorAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'funds', 'account_value' ,'date_joined', 'last_login')
    search_fields = ('is_admin',)
    readonly_fields = ('date_joined', 'last_login')

    ordering = ('last_login',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', )
    search_fields = ('is_admin',)
    readonly_fields = ()

    ordering = ('company_name',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class StockAdmin(admin.ModelAdmin):
    list_display = ('company',  'available_quantity','buy_price', 'sell_price')
    search_fields = ()
    readonly_fields = ()

    ordering = ('buy_price',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class AcquiredStockAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'stock', 'investors', )
    search_fields = ()
    readonly_fields = ()

    ordering = ('stock',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, UserAdmin)
admin.site.register(Investor, InvestorAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(AcquiredStock, AcquiredStockAdmin)


