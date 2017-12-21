

class PassPhrase:
    def __init__(self, passphrase):
        self.passphrase = passphrase

    def is_valid(self):
        raise NotImplementedError


if __name__ == '__main__':
    puzzle_input = ''
    passphrase = PassPhrase(puzzle_input)
