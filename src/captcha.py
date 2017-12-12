

class Captcha:
    @staticmethod
    def solve(digits):
        if len(digits) == 0:
            return 0
        total = 0
        for i in range(len(digits)-1):
            if digits[i] == digits[i+1]:
                total += int(digits[i])
        if digits[0] == digits[-1]:
            total += int(digits[0])
        return total


if __name__ == '__main__':
    puzzle_input = ''
    print(Captcha.solve(puzzle_input))
