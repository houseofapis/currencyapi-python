from unittest import TestCase

from currencyapi.endpoints.timeframe import Timeframe

class Test(TestCase):

    def setUp(self):
        self.class_under_test = Timeframe('fakekey')

    def test_timeframe_base(self):
        self.class_under_test.base('gBp')
        self.assertEqual('GBP', self.class_under_test.param.get('base'))
        self.assertIsInstance(self.class_under_test.base('uSD'), Timeframe)    

    def test_timeframe_start_date(self):
        self.class_under_test.start_date('2023-01-01')
        self.assertEqual('2023-01-01', self.class_under_test.param.get('start_date'))
        self.assertIsInstance(self.class_under_test.start_date('2023-01-01'), Timeframe)

    def test_timeframe_end_date(self):
        self.class_under_test.end_date('2023-01-02')
        self.assertEqual('2023-01-02', self.class_under_test.param.get('end_date'))
        self.assertIsInstance(self.class_under_test.end_date('2023-01-02'), Timeframe)

    def test_history_endpoint_set(self):
        self.assertEqual('timeframe', self.class_under_test.endpoint)