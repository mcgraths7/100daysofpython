from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)


def convert_to_datetime(line):
    """:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    timestamp = line.split(' ')[1]
    logdate = timestamp.split('T')[0].split('-')
    logtime = timestamp.split('T')[1].split(':')
    return datetime(int(logdate[0]), int(logdate[1]), int(logdate[2]), int(logtime[0]), int(logtime[1]),
                           int(logtime[2]))  # Returns datetime using year, month, day, hour, minute, second


def time_between_shutdowns(loglines):
    """
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    shutdown_events = [line for line in loglines if SHUTDOWN_EVENT in line]
    shutdown_timestamps = [convert_to_datetime(line) for line in shutdown_events]
    return shutdown_timestamps[-1] - shutdown_timestamps[0]  # Return the time between the last and first shutdown events


with open(logfile) as f:
    loglines = f.readlines()
    time_between_shutdowns(loglines)
