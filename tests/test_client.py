import unittest

from currencyapi import Client
from currencyapi.endpoints.rates import Rates

class Test(unittest.TestCase):
    def test_rates_method(self):
        errorMessage = "Rates method does not return rates object"
        class_under_test = Client('fakeKey')
        self.assertIsInstance(class_under_test.rates(), Rates, errorMessage)