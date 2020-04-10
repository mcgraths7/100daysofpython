# Pomodoro class - the timer is defined here


from datetime import datetime
from datetime import timedelta
import sys


def countdown(milliseconds):
    end_time = datetime.now() + timedelta(milliseconds=milliseconds)
    while True:
        delta = end_time - datetime.now()
        if delta < timedelta(0):
            break


class Pomodoro:
    def __init__(self):
        self.cycles_complete = 0
        self.current_task = ""
        self.define_task()

    def start_timer(self):
        while True:
            print(f"Starting task: {self.current_task}")
            countdown(milliseconds=1500000)
            self.cycles_complete += 1
            self.start_break()

    def start_break(self):
        if self.cycles_complete < 4:
            print("Time for a quick 5 minute break.")
            countdown(milliseconds=300000)
        else:
            print("Time for an extended, 20 minute break.")
            countdown(milliseconds=1200000)
            self.reset_timer()

    def reset_timer(self):
        self.cycles_complete = 0
        user_input = input("Looks like you've completed four cycles. Would you like to (r)epeat this task, "
                           "choose a (n)ew task, or (q)uit the timer?\n>>> ")
        if user_input == "r":
            self.start_timer()
        elif user_input == "n":
            self.define_task()
            self.start_timer()
        elif user_input == "q":
            sys.exit()
        else:
            print("Looks like that wasn't a valid input. Please try again (valid inputs are in parenthesis)")
            self.reset_timer()

    def define_task(self):
        self.current_task = input("Please let me know what your current task is...\n>>> ")


pom = Pomodoro()
pom.start_timer()