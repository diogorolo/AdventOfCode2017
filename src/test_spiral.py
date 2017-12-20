from unittest import TestCase
from src.spiral import Spiral


class TestSpiral(TestCase):
    def test_solve_same_spot(self):
        s = Spiral(1)
        result = s.solve()
        self.assertEqual(0, result)

    def test_solve_same_direction(self):
        s = Spiral(23)
        result = s.solve()
        self.assertEqual(2, result)

    def test_solve_diagonal(self):
        s = Spiral(12)
        result = s.solve()
        self.assertEqual(3, result)

    def test_solve_far(self):
        s = Spiral(1024)
        result = s.solve()
        self.assertEqual(31, result)
