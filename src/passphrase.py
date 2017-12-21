

class PassPhrase:
    def __init__(self, passphrase):
        self.passphrase = passphrase.strip('\n')

    def is_valid(self):
        tokens = self.passphrase.split(' ')
        return len(tokens) == len(set(tokens))


if __name__ == '__main__':
    with open('passphrases.txt', 'r') as f:
        passphrases = f.readlines()

    valid_passphrases = [p for p in passphrases if PassPhrase(p).is_valid()]
    print(len(valid_passphrases))
