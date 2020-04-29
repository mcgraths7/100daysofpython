import random


MAX_GUESSES = 5
START, END = 1, 20


def get_random_number():
    """Get a random number between 1 and 20"""
    return random.randint(START, END)


class Game:
    """Number guess class. Make it callable to initiate the game"""

    def __init__(self):
        self._guesses = set()
        self._answer = get_random_number()
        self._win = False

    def guess(self):
        """Ask user for input, convert to an int, and raise a ValueError outputting the following:
        'Please enter a number'
        'Should be a number'
        'Number not in range'
        'Already guessed'
        If all is good, return the int"""
        guess = input(f'Guess a number between {START} and {END}.\n')
        if not guess:
            raise ValueError('Please enter a number...')

        try:
            guess = int(guess)
        except ValueError:
            raise ValueError('Should be a number')

        if guess not in range(START, END + 1):
            raise ValueError('Number not in range')

        if guess in self._guesses:
            raise ValueError('Already guessed')

        self._guesses.add(guess)
        return guess

    def _validate_guess(self, guess):
        """Verify if guess is correct, print the following when applicable:
        '{guess} is correct!'
        '{guess} is too high'
        '{guess} is too low'
        returns a boolean"""
        if guess == self._answer:
            print(f'{guess} is correct!')
            return True
        else:
            high_or_low = 'low' if guess < self._answer else 'high'
            print(f'{guess} is too {high_or_low}')
            return False

    @property
    def num_guesses(self):
        return len(self._guesses)

    def __call__(self):
        """Entry point / game loop. Use a loop to break or continue
        see the tests for exact win lose messaging"""
        while len(self._guesses) < MAX_GUESSES:
            try:
                guess = self.guess()
            except ValueError as ve:
                print(ve)
                continue

            win = self._validate_guess(guess)
            if win:
                guess_str = self.num_guesses == 1 and 'guess' or 'guesses'
                print(f'It took you {self.num_guesses} {guess_str}')
                self._win = True
                break
        else:
            # else on while/for = anti pattern? useful in this case however.
            print(f'Guessed {self.num_guesses} times, answer was {self._answer}')


if __name__ == '__main__':
    game = Game()
    game()