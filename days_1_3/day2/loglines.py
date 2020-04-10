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
    logdatetime = datetime(int(logdate[0]), int(logdate[1]), int(logdate[2]), int(logtime[0]), int(logtime[1]),
                           int(logtime[2]))
    return logdatetime


def time_between_shutdowns(loglines):
    """
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    pass
    shutdown_events = [line for line in loglines if SHUTDOWN_EVENT in line]
    shutdown_timestamps = []
    for line in shutdown_events:
        shutdown_timestamps.append(convert_to_datetime(line))
    time_between_first_and_last_shutdown = shutdown_timestamps[-1] - shutdown_timestamps[0]
    return time_between_first_and_last_shutdown


with open(logfile) as f:
    loglines = f.readlines()
    time_between_shutdowns(loglines)
