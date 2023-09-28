from unittest import TestCase

from currencyapi.endpoints.convert import Convert

class Test(TestCase):

    def setUp(self):
        self.class_under_test = Convert('fakekey')

    def test_convert_from_currency(self):
        self.class_under_test.from_currency('gBp')
        self.assertEqual('GBP', self.class_under_test.param.get('from'))
        self.assertIsInstance(self.class_under_test.from_currency('uSD'), Convert)

    def test_convert_to_currency(self):
        self.class_under_test.to_currency('gBp')
        self.assertEqual('GBP', self.class_under_test.param.get('to'))
        self.assertIsInstance(self.class_under_test.to_currency('uSD'), Convert)

    def test_convert_amount(self):
        self.class_under_test.amount(10)
        self.assertEqual(10.00, self.class_under_test.param.get('amount'))
        self.assertIsInstance(self.class_under_test.amount(10), Convert)

    def test_history_endpoint_set(self):
        self.assertEqual('convert', self.class_under_test.endpoint)