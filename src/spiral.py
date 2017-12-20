from math import ceil, sqrt, copysign, floor


class Spiral:
    def __init__(self, number):
        self.number = number

    def matrix_size(self):
        result = ceil(sqrt(self.number))
        if result % 2 == 0:
            result += 1
        return result

    def side_distance(self):
        size = self.matrix_size()
        side_number = size*size

        for i in range(3):
            if side_number <= self.number:
                break
            side_number -= size - 1
        center_number = side_number + copysign(floor(size/2), self.number - side_number)
        distance = abs(self.number - center_number)
        return distance

    def solve(self):
        distance = self.side_distance() + floor(self.matrix_size() / 2)
        return distance


if __name__ == '__main__':
    puzzle_input = 368078
    spiral = Spiral(puzzle_input)
    print(spiral.solve())
