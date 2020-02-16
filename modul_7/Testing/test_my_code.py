from unittest import TestCase

from my_code import adding

class TestMyCode(TestCase):
    def test_add(self):
        result = adding(1, 2)
        self.assertEqual(result, 3)