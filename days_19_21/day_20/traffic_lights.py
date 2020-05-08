from itertools import cycle
from time import sleep
from sys import stdout


COLORS = cycle(['GREEN', 'AMBER', 'RED'])


def change_color(colors=COLORS, speed_limit=20):
    current_color = next(colors)
    stdout.write('\r' + current_color)
    stdout.flush()
    if current_color == 'RED':
        sleep(speed_limit / 2.5)
    elif current_color == 'AMBER':
        sleep(speed_limit / 10)
    elif current_color == 'GREEN':
        sleep(speed_limit / 2)


def main():
    while True:
        change_color()


if __name__ == '__main__':
    main()
