from unittest import TestCase

from currencyapi.endpoints.currencies import Currencies

class Test(TestCase):

    def setUp(self):
        self.class_under_test = Currencies('fakekey')

    def test_currencies_base(self):
        self.class_under_test.base('gBp')
        self.assertEqual('GBP', self.class_under_test.param.get('base'))
        self.assertIsInstance(self.class_under_test.base('uSD'), Currencies)

    def test_rates_endpoint_set(self):
        self.assertEqual('currencies', self.class_under_test.endpoint)