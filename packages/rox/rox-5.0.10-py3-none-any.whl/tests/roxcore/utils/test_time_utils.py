import unittest
from datetime import datetime
from rox.core.utils.time_utils import string_to_date

class StringToDateTests(unittest.TestCase):
    def test_time_with_mircoseconds(self):
        # non platform FM
        string_date = '2023-07-11T18:01:26.233334Z'
        self.assertEqual(string_to_date(string_date), datetime(2023, 7, 11, 18, 1, 26, 233334))

    def test_time_with_nanoseconds(self):
        # platfrom FM
        string_date = '2023-07-11T18:01:26.123233334Z'
        self.assertEqual(string_to_date(string_date), datetime(2023, 7, 11, 18, 1, 26))

    def test_time_with_full_seconds(self):
        string_date = '2023-07-11T18:01:26Z'
        self.assertEqual(string_to_date(string_date), datetime(2023, 7, 11, 18, 1, 26))

    def test_time_with_just_date(self):
        string_date = '2023-07-11'

        self.assertRaises(ValueError, string_to_date, string_date)

    def test_time_with_full_seconds(self):
        string_date = '2023-07-11T18:01:2aZ'

        self.assertRaises(ValueError, string_to_date, string_date)
