import sys
import time
import itertools


symbols = itertools.cycle(list('/-\|'))

while True:
    sys.stdout.write('\r' + next(symbols))
    sys.stdout.flush()
    time.sleep(.5)

