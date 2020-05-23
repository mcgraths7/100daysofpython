from datetime import datetime, timedelta
from winsound import Beep
import sys


def countdown(milliseconds):
    end_time = datetime.now() + timedelta(milliseconds=milliseconds)
    while True:
        delta = end_time - datetime.now()
        if delta < timedelta(0):
            break


class Pomodoro:
    def __init__(self):
        self.valid_inputs = {
            'r': self.__call__,
            'repeat': self.__call__,
            'n': self.define_task,
            'new': self.define_task,
            'q': sys.exit,
        }
        self.cycles_complete = 0
        self.beep_frequency = 2500
        self.beep_duration = 250
        self.current_task = ""
        self.define_task()

    def __call__(self):
        """Entry point for the app, gets called when run from the command line"""
        while True:
            print(f"{datetime.now()} Starting task: {self.current_task}")
            countdown(milliseconds=1500000)
            self.cycles_complete += 1
            self.start_break()

    def start_break(self):
        Beep(self.beep_frequency, self.beep_duration)
        if self.cycles_complete < 4:
            print(f"{datetime.now()} Time for a quick 5 minute break.")
            countdown(milliseconds=300000)
        else:
            print(f"{datetime.now()} Time for an extended, 20 minute break.")
            countdown(milliseconds=1200000)
            self.reset_timer()

    def get_valid_input(self, user_input):
        inp = self.valid_inputs.get(user_input)
        if inp is None:
            raise ValueError('Not a valid input, please try again (valid inputs are in parenthesis)')
        return inp

    def reset_timer(self):
        self.cycles_complete = 0
        user_input = input(f"{datetime.now()} Looks like you have completed four cycles. Would you like to "
                           "(r)epeat this task, choose a (n)ew task, or (q)uit the timer?\n>>> ")

        try:
            self.get_valid_input(user_input)()
        except ValueError as ve:
            print(ve)
            self.reset_timer()

    def define_task(self):
        self.current_task = input("Please let me know what your current task is...\n>>> ")
        self.__call__()


if __name__ == '__main__':
    pomodoro = Pomodoro()
    pomodoro()