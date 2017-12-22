from unittest import TestCase
from src.cpu_maze import CpuMaze


class TestCpuMaze(TestCase):
    def setUp(self):
        data = '0 3 0 1 -3'
        data = data.split(' ')
        self.c = CpuMaze(data)

    def test_init(self):
        self.assertEqual(0, self.c.instruction(0))
        self.assertEqual(3, self.c.instruction(1))
        self.assertEqual(0, self.c.instruction(2))
        self.assertEqual(1, self.c.instruction(3))
        self.assertEqual(-3, self.c.instruction(4))

    def test_jump_increment(self):
        cur_value = self.c.instruction(0)
        self.c.jump()
        self.assertEqual(cur_value + 1, self.c.instruction(0))

    def test_jump_idx_change(self):
        self.c.jump()
        self.assertEqual(0, self.c.current_idx)
        self.c.jump()
        self.assertEqual(1,self.c.current_idx)

    def test_solve(self):
        total_iterations = self.c.solve()
        self.assertEqual(5, total_iterations)
