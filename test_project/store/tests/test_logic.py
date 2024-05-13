from django.test import TestCase
from store.tests.logic import operations

class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(6, 2, '+')
        self.assertEqual(8, result)

    def test_minus(self):
        result = operations(6, 2, '-')
        self.assertEqual(4, result)

    def test_multi(self):
        result = operations(7, 3, '*')
        self.assertEqual(21, result)