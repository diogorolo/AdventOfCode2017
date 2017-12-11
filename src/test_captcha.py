from unittest import TestCase
from captcha import Captcha


class TestCaptcha(TestCase):
    def setUp(self):
        self.c = Captcha()

    def test_solver_all_equal(self):
        result = self.c.solve('1111')
        self.assertEqual(4, result)

    def test_solver_all_different(self):
        result = self.c.solve('1234')
        self.assertEqual(0, result)

    def test_solver_simple_sums(self):
        result = self.c.solve('1122')
        self.assertEqual(3, result)

    def test_loop_sum(self):
        result = self.c.solve('91212129')
        self.assertEqual(9, result)

    def test_multiple_sums(self):
        result = self.c.solve('911229')
        self.assertEqual(12, result)
