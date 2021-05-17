from django.test import TestCase
from .models import *
from django.test import Client
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your tests here.


class InvestorModelTests(TestCase):
    def test_funds_too_big(self):
        investor = Investor(funds=10**20)
        self.assertIs(investor.validFunds(), False)

    def test_funds_negative(self):
        investor = Investor(funds=-100)
        self.assertIs(investor.validFunds(), False)


class StockModelTests(TestCase):
    def test_buy_value_too_big(self):
        stock = Stock(sell_price=10**20)
        self.assertIs(stock.validPrice(), False)

    def test_sell_value_too_big(self):
        stock = Stock(sell_price=-100)
        self.assertIs(stock.validPrice(), False)

    def test_buy_value_negative(self):
        stock = Stock(sell_price=10**20)
        self.assertIs(stock.validPrice(), False)

    def test_sell_value_negative(self):
        stock = Stock(sell_price=-100)
        self.assertIs(stock.validPrice(), False)

    def test_available_quantity_too_big(self):
        stock = Stock(available_quantity=10**20)
        self.assertIs(stock.validQuantity(), False)

    def test_available_quantity_negative(self):
        stock = Stock(available_quantity=-100)
        self.assertIs(stock.validQuantity(), False)


class AcquiredStockTests(TestCase):
    def test_quantity_too_big(self):
        acqstock = AcquiredStock(quantity=10**20)
        self.assertIs(acqstock.validQuantity(), False)

    def test_quantity_negative(self):
        acqstock = AcquiredStock(quantity=-100)
        self.assertIs(acqstock.validQuantity(), False)


class CustomUserTestCase(TestCase):
    def test_login_user(self):
        c = Client()
        response = c.post(reverse('login'), {"email" : "testuser@gmail.com", "password" : "123ana123"})

        self.assertEqual(response.status_code, 200)

    def test_register_investor(self):
        c = Client()
        response = c.post(reverse('registerUser'), {"first_name": "Test", "last_name":"User","email": "testuser@gmail.com", "password": "123ana123"})

        self.assertEqual(response.status_code, 302)

    def test_register_company(self):
        c = Client()
        response = c.post(reverse('registerCompany'), {"company_name": "Test Company","email": "testuser@gmail.com", "password": "123ana123"})

        self.assertEqual(response.status_code, 302)

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


class InvestorViewsTest(TestCase):
    def test_depositmoney(self):
        user = User.objects.create_user(email="testuser@gmail.com", password="123ana123")
        inv = Investor(user=user)

        self.client.login(email="testuser@gmail.com", password="123ana123")
        response = self.client.get('/depositmoney/')


        self.assertEqual(response.status_code, 200)

    def test_withdrawmoney(self):
        user = User.objects.create_user(email="testuser@gmail.com", password="123ana123")
        inv = Investor(user=user)
        self.client.login(email="testuser@gmail.com", password="123ana123")
        response = self.client.get('/withdrawmoney/')
        self.assertEqual(response.status_code, 200)

    def test_buyshares(self):
        user = User.objects.create_user(email="testuser@gmail.com", password="123ana123")
        inv = Investor(user=user)
        self.client.login(email="testuser@gmail.com", password="123ana123")
        response = self.client.get('/buyshares/')
        self.assertEqual(response.status_code, 200)

    def test_sellshares(self):
        user = User.objects.create_user(email="testuser@gmail.com", password="123ana123")
        inv = Investor(user=user)
        self.client.login(email="testuser@gmail.com", password="123ana123")
        response = self.client.get('/sellshares/')
        self.assertEqual(response.status_code, 200)

    def test_checkfunds(self):
        user = User.objects.create_user(email="testuser@gmail.com", password="123ana123")
        inv = Investor(user=user)
        self.client.login(email="testuser@gmail.com", password="123ana123")
        response = self.client.get('/checkfunds/')
        self.assertEqual(response.status_code, 200)

    def test_homeinvestor(self):
        user = User.objects.create_user(email="testuser@gmail.com", password="123ana123")
        inv = Investor(user=user)
        self.client.login(email="testuser@gmail.com", password="123ana123")
        response = self.client.get('/homeinvestor/')
        self.assertEqual(response.status_code, 200)


class CompanyViewsTest(TestCase):
    def test_addshares(self):
        user = User.objects.create_user(email="testuser@gmail.com", password="123ana123")
        comp = Company(user=user)

        self.client.login(email="testuser@gmail.com", password="123ana123")

        response = self.client.get('/addshares/')
        self.assertEqual(response.status_code, 200)

    def test_removeshares(self):
        user = User.objects.create_user(email="testuser@gmail.com", password="123ana123")
        comp = Company(user=user)

        self.client.login(email="testuser@gmail.com", password="123ana123")

        response = self.client.get('/removeshares/')
        self.assertEqual(response.status_code, 200)

    def test_homecompany(self):
        user = User.objects.create_user(email="testuser@gmail.com", password= "123ana123")
        comp = Company(user = user)

        self.client.login(email="testuser@gmail.com", password= "123ana123")

        response = self.client.get('/homecompany/')
        self.assertEqual(response.status_code, 200)
