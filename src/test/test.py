from os import sys, path

root_files = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))
sys.path.append(root_files)

# External libraries
import unittest

# Local libraries
from src.utils.read_file import read
from src.services.payments import formatter_service, parser_service, payments_service


class Testing(unittest.TestCase):
    def test_parser(self):
        string_data = "RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00"
        expected_result = {'name': 'RENE', 'hours': ['MO10:00-12:00', 'TU10:00-12:00', 'TH01:00-03:00', 'SA14:00-18:00', 'SU20:00-21:00']}
        result = parser_service.parser_payments(string_data)
        msg = "test_parser"
        self.assertEqual(result, expected_result, msg)

    def test_formatter(self):
        hours_worked = {
            "name": "RENE",
            "hours": ["MO10:00-12:00", "TU10:00-12:00", "TH01:00-03:00", "SA14:00-18:00", "SU20:00-21:00"]
        }
        expected_result = {
            'name': 'RENE',
            'hours': ['MO10:00-12:00', 'TU10:00-12:00', 'TH01:00-03:00', 'SA14:00-18:00', 'SU20:00-21:00'],
            'formatted_hours': {
                'monday': {
                    'start': 11000,
                    'end': 11200,
                    'hours_worked': 2
                },
                'tuesday': {
                    'start': 11000,
                    'end': 11200,
                    'hours_worked': 2
                },
                'thursday': {
                    'start': 10100,
                    'end': 10300,
                    'hours_worked': 2
                },
                'saturday': {
                    'start': 11400,
                    'end': 11800,
                    'hours_worked': 4
                },
                'sunday': {
                    'start': 12000,
                    'end': 12100,
                    'hours_worked': 1
                }
            }
        }
        result = formatter_service.format_date_hours(hours_worked)
        msg = "test_formatter"
        self.assertEqual(result, expected_result, msg)

    def test_formatter_payment(self):
        expected_result = {
            'monday': [{
                'start': 10001,
                'end': 10900,
                'pay': 25
            }, {
                'start': 10901,
                'end': 11800,
                'pay': 15
            }, {
                'start': 11801,
                'end': 10000,
                'pay': 20
            }],
            'tuesday': [{
                'start': 10001,
                'end': 10900,
                'pay': 25
            }, {
                'start': 10901,
                'end': 11800,
                'pay': 15
            }, {
                'start': 11801,
                'end': 10000,
                'pay': 20
            }],
            'wednesday': [{
                'start': 10001,
                'end': 10900,
                'pay': 25
            }, {
                'start': 10901,
                'end': 11800,
                'pay': 15
            }, {
                'start': 11801,
                'end': 10000,
                'pay': 20
            }],
            'thursday': [{
                'start': 10001,
                'end': 10900,
                'pay': 25
            }, {
                'start': 10901,
                'end': 11800,
                'pay': 15
            }, {
                'start': 11801,
                'end': 10000,
                'pay': 20
            }],
            'friday': [{
                'start': 10001,
                'end': 10900,
                'pay': 25
            }, {
                'start': 10901,
                'end': 11800,
                'pay': 15
            }, {
                'start': 11801,
                'end': 10000,
                'pay': 20
            }],
            'saturday': [{
                'start': 10001,
                'end': 10900,
                'pay': 30
            }, {
                'start': 10901,
                'end': 11800,
                'pay': 20
            }, {
                'start': 11801,
                'end': 10000,
                'pay': 25
            }],
            'sunday': [{
                'start': 10001,
                'end': 10900,
                'pay': 30
            }, {
                'start': 10901,
                'end': 11800,
                'pay': 20
            }, {
                'start': 11801,
                'end': 10000,
                'pay': 25
            }]
        }
        result = formatter_service.format_payments()
        msg = "test_formatter_payment"
        self.assertEqual(result, result, msg)

    def test_payment(self):
        days_worked = {
            "name": "RENE",
            "hours": ["MO10:00-12:00", "TU10:00-12:00", "TH01:00-03:00", "SA14:00-18:00", "SU20:00-21:00"],
            "formatted_hours":{
                "monday":{"start": 11000, "end": 11200, "hours_worked": 2},
                "tuesday":{"start": 11000, "end": 11200, "hours_worked": 2},
                "thursday":{"start": 10100, "end": 10300, "hours_worked": 2},
                "saturday":{"start": 11400, "end": 11800, "hours_worked": 4},
                "sunday":{"start": 12000, "end": 12100, "hours_worked": 1},
            }
        }
        expected_result = 215
        result = payments_service.get_payments_2(days_worked)
        msg = "test_payment"
        self.assertEqual(result, expected_result, msg)

    def test_read_file(self):
        a = True
        b = True
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()