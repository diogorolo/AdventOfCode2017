from unittest import TestCase
from src.reallocation import Reallocation


class TestReallocation(TestCase):
    def setUp(self):
        input_data = [int(x) for x in '0 2 7 0'.split(' ')]
        self.r = Reallocation(input_data)

    def test_distribute(self):
        self.r.distribute()
        self.assertEqual([2, 4, 1, 2], self.r.current_state)

    def test_save_state(self):
        self.r.distribute()
        self.assertEqual([2, 4, 1, 2], self.r.memory[0])

    def test_solve(self):
        result = self.r.solve()
        self.assertEqual(5, result)

    def test_largest_memory_idx(self):
        self.assertEqual(2, self.r.largest_memory_idx())

    def test_largest_memory_idx_repeated_values(self):
        input_data = [int(x) for x in '7 2 7 0'.split(' ')]
        self.r = Reallocation(input_data)
        self.assertEqual(0, self.r.largest_memory_idx())
