from unittest import TestCase
from checksum import Checksum


class TestChecksum(TestCase):
    def test_differenceInRow(self):
        input_data = ("5 1 9 5\r\n"
                      "7 5 3\r\n"
                      "2 4 6 8")
        c = Checksum(input_data)
        self.assertEqual(8, c.line_difference(0))
        self.assertEqual(4, c.line_difference(1))
        self.assertEqual(6, c.line_difference(2))

    def test_totalChecksum(self):
        input_data = ("5 1 9 5\r\n"
                      "7 5 3\r\n"
                      "2 4 6 8")
        c = Checksum(input_data)
        self.assertEqual(18, c.solve())

    def test_parseInput(self):
        input_data = ("5 1 9 5\r\n"
                      "7 5 3\r\n"
                      "2 4 6 8")

        c = Checksum(input_data)
        expected_data = [[5, 1, 9, 5],
                         [7, 5, 3],
                         [2, 4, 6, 8]]

        self.assertEqual(expected_data, c.matrix)

    def test_emptyInput(self):
        input_data = ''
        c = Checksum(input_data)
        self.assertEqual(0, c.solve())
