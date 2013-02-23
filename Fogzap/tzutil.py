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
    crossed."""

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

class UTC(datetime.tzinfo):
    """UTC class from the tzinfo documentation quoted in: http://stackoverflow.com/questions/2331592/datetime-datetime-utcnow-why-no-tzinfo"""

    def utcoffset(self, dt):
        return ZERO

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return ZERO

