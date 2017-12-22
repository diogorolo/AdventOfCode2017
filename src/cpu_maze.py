

class CpuMaze:
    def __init__(self, instruction_data):
        self.instructions = [int(x.strip('\r\n')) for x in instruction_data]
        self.current_idx = 0

    def instruction(self, idx):
        return self.instructions[idx]

    def jump(self):
        pass

    def solve(self):
        pass


if __name__ == '__main__':
    with open('cpu_instructions_Data.txt', 'r') as f:
        instructions = f.readlines()

    c = CpuMaze(instructions)
    print(c.solve())