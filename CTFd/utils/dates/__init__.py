import datetime
import time

from CTFd.utils import get_config


def ctftime():
    """ Checks whether it's CTF time or not. """

    start = get_config("start")
    end = get_config("end")

    if start:
        start = int(start)
    else:
        start = 0
    if end:
        end = int(end)
    else:
        end = 0

    if start and end:
        if start < time.time() < end:
            # Within the two time bounds
            return True

    if start < time.time() and end == 0:
        # CTF starts on a date but never ends
        return True

    if start == 0 and time.time() < end:
        # CTF started but ends at a date
        return True

    if start == 0 and end == 0:
        # CTF has no time requirements
        return True

    return False


def ctf_paused():
    return get_config("paused")


def ctf_started():
    return time.time() > int(get_config("start") or 0)


def ctf_ended():
    if int(get_config("end") or 0):
        return time.time() > int(get_config("end") or 0)
    return False


def view_after_ctf():
    return get_config("view_after_ctf")


def unix_time(dt):
    return int((dt - datetime.datetime(1970, 1, 1)).total_seconds())


def unix_time_millis(dt):
    return unix_time(dt) * 1000


def unix_time_to_utc(t):
    return datetime.datetime.utcfromtimestamp(t)


def isoformat(dt):
    return dt.isoformat() + "Z"


def dark_time():
    """ Checks whether it's Dark Light time or not. """

    end = get_config("end")
    dark_time = get_config("dark_time")

    if end:
        end = int(end)
    else:
        end = 0
    if dark_time:
        dark_time = int(dark_time)
        # if dark_time is 0, it is always light
        if dark_time == 0:
            return False
    else:
        # if dark_time is not set, it is always light
        return False

    if dark_time and end:
        if (end - dark_time) < time.time() < end:
            # Within the two time bounds
            return True

    return False
