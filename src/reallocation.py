

class Reallocation:
    def __init__(self, memory_blocks):
        self.current_state = memory_blocks
        self.memory = []

    def largest_memory_idx(self):
        max_val = max(self.current_state)
        for idx, val in enumerate(self.current_state):
            if val == max_val:
                return idx

    def distribute(self):
        pass

    def save_state(self):
        self.memory.append(self.current_state)

    def is_repeated_state(self):
        return self.current_state in self.memory

    def solve(self):
        pass


if __name__ == '__main__':
    input_data = [int(x) for x in '0 2 7 0'.split(' ')]
    r = Reallocation(input_data)
    print(r.solve())
