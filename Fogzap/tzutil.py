# Local and UTC timezone (tzinfo) classes from Python 2 datetime documentation 
import datetime
from datetime import timedelta
import time as _time

ZERO = timedelta(0)
STDOFFSET = timedelta(seconds = -_time.timezone)
if _time.daylight:
    DSTOFFSET = timedelta(seconds = -_time.altzone)
else:
    DSTOFFSET = STDOFFSET

DSTDIFF = DSTOFFSET - STDOFFSET

class LocalTimezone(datetime.tzinfo):
    """Local timezone as worked together in they Python 2 documentation for the datetime class.

    Probably has bugs where it doesn't work if the program is running
    while a daylight savings time or other time-zone irregularity is
    crossed.

    I've also added some extra methods not in the original: now and in_future

    """

    def utcoffset(self, dt):
        if self._isdst(dt):
            return DSTOFFSET
        else:
            return STDOFFSET

    def dst(self, dt):
        if self._isdst(dt):
            return DSTDIFF
        else:
            return ZERO

    def tzname(self, dt):
        return _time.tzname[self._isdst(dt)]

    def _isdst(self, dt):
        tt = (dt.year, dt.month, dt.day,
              dt.hour, dt.minute, dt.second,
              dt.weekday(), 0, 0)
        stamp = _time.mktime(tt)
        tt = _time.localtime(stamp)
        return tt.tm_isdst > 0

    def now(self):
        """Return a timezone aware datetime.datetime that represents the current microsecond"""
        return datetime.datetime.now(LocalTimezone())

    def in_future(self, a_datetime):
        """Return true if a_datetime comes strictly after the current microsecond.
        
        a_datetime must be a timezone aware datetime.datetime object

        Note: there is a bit of a race condition in this code because
        I have to calculate the 'now' object before I can compare it
        to a_datetime. Thus if a_datetime lies in the interval between
        the time the function is called and the time the instant of
        the 'now' object is fixed this will return (incorrectly) that
        a_datetime is not in the future. Another source of error is
        system clock resolution and accuracy. For most applications,
        this is completely inconsequential, but consider yourself
        warned.

        """
        return a_datetime > self.now()

class UTC(datetime.tzinfo):
    """UTC class from the tzinfo documentation quoted in: http://stackoverflow.com/questions/2331592/datetime-datetime-utcnow-why-no-tzinfo"""

    def utcoffset(self, dt):
        return ZERO

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return ZERO

def is_naive(a_datetime):
    """Return true iff a_datetime is timezone naive (see datetime docs)

    timezone aware is the opposite of timezone naive.

    a_datetime - an instance of datetime.datetime
    """
    return (a_datetime.tzinfo is None or 
            a_datetime.tzinfo.utcoffset(a_datetime) is None)
