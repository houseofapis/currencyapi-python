from unittest import TestCase
from unittest.mock import Mock, patch
from currencyapinet.endpoints.ohlc import Ohlc
import requests

class Test(TestCase):

    def setUp(self):
        self.class_under_test = Ohlc('fakekey')

    def test_ohlc_currency(self):
        self.class_under_test.currency('eUr')
        self.assertEqual('EUR', self.class_under_test.param.get('currency'))
        self.assertIsInstance(self.class_under_test.currency('EUR'), Ohlc)

    def test_ohlc_date(self):
        self.class_under_test.date('2023-12-25')
        self.assertEqual('2023-12-25', self.class_under_test.param.get('date'))
        self.assertIsInstance(self.class_under_test.date('2023-12-25'), Ohlc)

    def test_ohlc_base(self):
        self.class_under_test.base('gBp')
        self.assertEqual('GBP', self.class_under_test.param.get('base'))
        self.assertIsInstance(self.class_under_test.base('USD'), Ohlc)

    def test_ohlc_interval(self):
        self.class_under_test.interval('1h')
        self.assertEqual('1h', self.class_under_test.param.get('interval'))
        self.assertIsInstance(self.class_under_test.interval('1d'), Ohlc)

    def test_ohlc_endpoint_set(self):
        self.assertEqual('ohlc', self.class_under_test.endpoint)

    def test_ohlc__build_url_params(self):
        self.assertDictEqual(
            {'key': 'fakekey', 'output': 'JSON'},
            self.class_under_test._build_url_params()
        )
        self.class_under_test.currency('EUR')
        self.class_under_test.date('2023-12-25')
        self.assertDictEqual(
            {'key': 'fakekey', 'output': 'JSON', 'currency': 'EUR', 'date': '2023-12-25'},
            self.class_under_test._build_url_params()
        )
        self.class_under_test.base('gbP')
        self.class_under_test.interval('1h')
        self.assertDictEqual(
            {'key': 'fakekey', 'output': 'JSON', 'currency': 'EUR', 'date': '2023-12-25', 'base': 'GBP', 'interval': '1h'},
            self.class_under_test._build_url_params()
        )

    @patch.object(requests, 'get')
    def test_ohlc_get(self, mock_requests_get):
        mock_data = [{"id": 1}, {"id": 2}]
        response_mock = Mock(return_value=mock_data)
        mock_requests_get.return_value.json = response_mock
        self.assertEqual(
            mock_data,
            self.class_under_test.get()
        )

    @patch.object(requests, 'get')
    def test_ohlc_get_xml(self, mock_requests_get):
        self.class_under_test.output('xMl')
        mock_data = [{"id": 1}, {"id": 2}]
        mock_requests_get.return_value.text = mock_data
        self.assertEqual(
            mock_data,
            self.class_under_test.get()
        )
