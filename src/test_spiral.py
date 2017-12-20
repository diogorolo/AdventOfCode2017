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

    def test_matrix_size_same_spot(self):
        s = Spiral(1)
        result = s.matrix_size()
        self.assertEqual(1, result)

    def test_matrix_size_one_away(self):
        s = Spiral(8)
        result = s.matrix_size()
        self.assertEqual(3, result)

    def test_matrix_size_four_away(self):
        s = Spiral(26)
        result = s.matrix_size()
        self.assertEqual(7, result)

    def test_side_distance_centered(self):
        s = Spiral(11)
        result = s.side_distance()
        self.assertEqual(0, result)

    def test_side_distance_one_offset(self):
        s = Spiral(3)
        result = s.side_distance()
        self.assertEqual(1, result)

    def test_side_distance_corner(self):
        s = Spiral(25)
        result = s.side_distance()
        self.assertEqual(2, result)
