from unittest import TestCase

from currencyapi.endpoints.history import History

class Test(TestCase):

    def setUp(self):
        self.class_under_test = History('fakekey')

    def test_history_base(self):
        self.class_under_test.base('gBp')
        self.assertEqual('GBP', self.class_under_test.param.get('base'))
        self.assertIsInstance(self.class_under_test.base('uSD'), History)    

    def test_history_date(self):
        self.class_under_test.date('2023-01-01')
        self.assertEqual('2023-01-01', self.class_under_test.param.get('date'))
        self.assertIsInstance(self.class_under_test.date('2023-01-01'), History)

    def test_history_endpoint_set(self):
        self.assertEqual('history', self.class_under_test.endpoint)