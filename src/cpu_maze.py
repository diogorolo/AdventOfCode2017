

class CpuMaze:
    def __init__(self, instruction_data):
        self.instructions = [int(x.strip('\r\n')) for x in instruction_data]
        self.current_idx = 0

    def instruction(self, idx):
        return self.instructions[idx]

    def jump(self):
        self.instructions[self.current_idx] += 1
        self.current_idx += self.instructions[self.current_idx] - 1

    def solve(self):
        iterations = 0
        while self.current_idx < len(self.instructions):
            iterations += 1
            self.jump()
        return iterations


if __name__ == '__main__':
    with open('cpu_instructions_data.txt', 'r') as f:
        instructions = f.readlines()

    c = CpuMaze(instructions)
    print(c.solve())
