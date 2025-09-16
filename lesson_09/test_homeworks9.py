import unittest
from lesson_09.homework9_code import warehouse, payment, balck_sea


class TestWarehouse(unittest.TestCase):

    def test_default_values(self):
        self.assertEqual(warehouse(), (152341, 98108, 124842))

    def test_zero_total(self):
        self.assertEqual(warehouse(0, 0, 0), (0, 0, 0))

    def test_only_first_and_second(self):
        self.assertEqual(warehouse(100, 100, 0), (100, 0, 0))

    def test_only_second_and_third(self):
        self.assertEqual(warehouse(100, 0, 100), (0, 0, 100))

    def test_not_equal_case(self):
        self.assertNotEqual(warehouse(), (0, 0, 0))

class TestPayment(unittest.TestCase):

    def test_default_payment(self):
        self.assertEqual(payment(), 21222)

    def test_one_month(self):
        self.assertEqual(payment(2000, 1), 2000)

    def test_zero_months(self):
        self.assertEqual(payment(2000, 0), 0)

    def test_zero_payment(self):
        self.assertEqual(payment(0, 12), 0)


class TestBlackSea(unittest.TestCase):

    def test_default_sum(self):
        self.assertEqual(balck_sea(), 474202)

    def test_zero_values(self):
        self.assertEqual(balck_sea(0, 0), 0)

    def test_negative_value(self):
        self.assertEqual(balck_sea(-100, 50), -50)

    def test_not_equal_wrong_result(self):
        self.assertNotEqual(balck_sea(), 0)
