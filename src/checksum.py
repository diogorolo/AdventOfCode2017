

class Checksum:
    def __init__(self, matrix_text):
        self.matrix = self.__parse(self.__sanitize(matrix_text))

    def __sanitize(self,matrix_text):
        return matrix_text.replace('\t', ' ').replace('\r\n', '\n')

    def __parse(self, matrix_text):
        return [list(map(int, x.split(' '))) for x in matrix_text.split('\n') if x != '']

    def solve(self):
        result = 0
        for i in range(len(self.matrix)):
            result += self.line_difference(i)
        return result

    def line_difference(self, line_idx):
        line = self.matrix[line_idx]
        return max(line) - min(line)


if __name__ == '__main__':
    puzzle_input = ''
    checksum_solver = Checksum(puzzle_input)
    print(checksum_solver.solve())
