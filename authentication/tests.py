from django.test import TestCase
from .models import *

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