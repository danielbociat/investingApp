from django import forms
from django.contrib.auth.forms import UserCreationForm
from authentication.models import User, Investor, Company


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class RegisterInvestorForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = Investor
        fields = ('first_name', 'last_name')


class RegisterCompanyForm(forms.ModelForm):
    company_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = Company
        fields = ('company_name',)
