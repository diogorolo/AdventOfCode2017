

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
        start_idx = self.largest_memory_idx()
        memory_amount = self.current_state[start_idx]
        self.current_state[start_idx] = 0
        start_idx += 1
        for i in range(memory_amount):
            self.current_state[(start_idx + i) % len(self.current_state)] += 1
        if self.is_repeated_state():
            return False

        self.save_state()
        return True

    def save_state(self):
        self.memory.append(list(self.current_state))

    def is_repeated_state(self):
        return self.current_state in self.memory

    def solve(self):
        iterations = 1
        while self.distribute():
            iterations += 1
        return iterations

if __name__ == '__main__':
    input_data = [int(x) for x in '0 2 7 0'.split(' ')]
    r = Reallocation(input_data)
    print(r.solve())
