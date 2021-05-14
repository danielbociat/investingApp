from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.conf import settings

# Create your models here.

class MyAccountManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user





class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = None
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    object = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Investor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  primary_key=True)

    first_name = models.CharField(verbose_name="first name", max_length=60, default="Missing")
    last_name = models.CharField(verbose_name="last name", max_length=60, default="Missing")

    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)

    funds = models.DecimalField(verbose_name="funds", default=0, max_digits=19, decimal_places=2)


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(verbose_name="company name", max_length=60, default="Missing")


class Stock(models.Model):
    company = models.OneToOneField(Company,on_delete=models.CASCADE, primary_key=True)
    #name = models.CharField(verbose_name="name", max_length=6, default="XXXXXX", unique=True)
    buy_price = models.DecimalField(verbose_name="buy price", max_digits=19, decimal_places=2)
    sell_price = models.DecimalField(verbose_name="sell price", max_digits=19, decimal_places=2)


class AcquiredStock(models.Model):
    quantity = models.IntegerField(verbose_name="quantity")
    stock = models.OneToOneField(Stock, verbose_name="stock", on_delete=models.CASCADE, primary_key=True)

    investors = models.ForeignKey(Investor, on_delete=models.SET_NULL, null=True)



