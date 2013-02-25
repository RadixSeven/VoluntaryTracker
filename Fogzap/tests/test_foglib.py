from foglib import fogbugz_datetime
import types
import unittest
from foglib import Interval
from foglib import BoundedTimeInterval
from foglib import OngoingTimeInterval
from foglib import Session

import tzutil
import datetime

def datetime_from_19_char_string(s):
    """String in format: '20130221_0107030500'
                          YYYYMMDD_HHmmSStimz
                          0123456789012345678
                                    111111111

    The time zone is negative so 0500 would -5 hours and 0 minutes

    """
    year = int(s[0:4])
    month = int(s[4:6])
    day = int(s[6:8])
    hour = int(s[9:11])
    minute = int(s[11:13])
    second = int(s[13:15])
    tz_hour = -int(s[15:17])
    tz_min  = -int(s[17:19])

    class tz(datetime.tzinfo):
        def utcoffset(self, dt):
            return datetime.timedelta(hours = tz_hour, minutes = tz_min)

        def dst(self, dt):
            return timedelta(0)

        def tzname(self, dt):
            return None
    
    try:
        return datetime.datetime(year, month, day, hour, minute, 
                                 second, 0, tz())
    except ValueError as e:
        raise ValueError("Original message: '{}' params: {} {} {} {} {} {}"
                         .format(str(e), year, month, day, hour, minute, second)
                         )

    
class TestFogbugzDatetime(unittest.TestCase):
    def test_fogbugz_datetime_returns_20130221_0500000000_for_20130221T050000Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T05:00:00Z')))

    def test_fogbugz_datetime_returns_20130221_0500000000_for_20130221T050000Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T05:00:00Z')))

    def test_fogbugz_datetime_returns_20130221_0606500000_for_20130221T060650Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T06:06:50Z')))

    def test_fogbugz_datetime_returns_20130221_0606500000_for_20130221T060650Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T06:06:50Z')))

    def test_fogbugz_datetime_returns_20130221_0607030000_for_20130221T060703Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T06:07:03Z')))

    def test_fogbugz_datetime_returns_20130221_0607030000_for_20130221T060703Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T06:07:03Z')))

    def test_fogbugz_datetime_returns_20130221_1025000000_for_20130221T102500Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T10:25:00Z')))

    def test_fogbugz_datetime_returns_20130221_1025000000_for_20130221T102500Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T10:25:00Z')))

    def test_fogbugz_datetime_returns_20130221_1025000000_for_20130221T102500Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T10:25:00Z')))

    def test_fogbugz_datetime_returns_20130221_1025000000_for_20130221T102500Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T10:25:00Z')))

    def test_fogbugz_datetime_returns_20130221_1051060000_for_20130221T105106Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T10:51:06Z')))

    def test_fogbugz_datetime_returns_20130221_1051060000_for_20130221T105106Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T10:51:06Z')))

    def test_fogbugz_datetime_returns_20130221_1804000000_for_20130221T180400Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T18:04:00Z')))

    def test_fogbugz_datetime_returns_20130221_1804000000_for_20130221T180400Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T18:04:00Z')))

    def test_fogbugz_datetime_returns_20130221_1825000000_for_20130221T182500Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T18:25:00Z')))

    def test_fogbugz_datetime_returns_20130221_1825000000_for_20130221T182500Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T18:25:00Z')))

    def test_fogbugz_datetime_returns_20130221_1825000000_for_20130221T182500Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T18:25:00Z')))

    def test_fogbugz_datetime_returns_20130221_1825000000_for_20130221T182500Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T18:25:00Z')))

    def test_fogbugz_datetime_returns_20130221_1831090000_for_20130221T183109Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T18:31:09Z')))

    def test_fogbugz_datetime_returns_20130221_1831090000_for_20130221T183109Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T18:31:09Z')))

    def test_fogbugz_datetime_returns_20130221_1831090000_for_20130221T183109Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T18:31:09Z')))

    def test_fogbugz_datetime_returns_20130221_1831090000_for_20130221T183109Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T18:31:09Z')))

    def test_fogbugz_datetime_returns_20130221_1845410000_for_20130221T184541Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T18:45:41Z')))

    def test_fogbugz_datetime_returns_20130221_1845410000_for_20130221T184541Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T18:45:41Z')))

    def test_fogbugz_datetime_returns_20130221_1846100000_for_20130221T184610Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T18:46:10Z')))

    def test_fogbugz_datetime_returns_20130221_1846100000_for_20130221T184610Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T18:46:10Z')))

    def test_fogbugz_datetime_returns_20130221_1907160000_for_20130221T190716Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T19:07:16Z')))

    def test_fogbugz_datetime_returns_20130221_1907160000_for_20130221T190716Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T19:07:16Z')))

    def test_fogbugz_datetime_returns_20130221_1907160000_for_20130221T190716Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T19:07:16Z')))

    def test_fogbugz_datetime_returns_20130221_1907160000_for_20130221T190716Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T19:07:16Z')))

    def test_fogbugz_datetime_returns_20130221_1932300000_for_20130221T193230Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T19:32:30Z')))

    def test_fogbugz_datetime_returns_20130221_1932300000_for_20130221T193230Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T19:32:30Z')))

    def test_fogbugz_datetime_returns_20130221_1932300000_for_20130221T193230Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T19:32:30Z')))

    def test_fogbugz_datetime_returns_20130221_1932300000_for_20130221T193230Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T19:32:30Z')))

    def test_fogbugz_datetime_returns_20130221_2032380000_for_20130221T203238Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T20:32:38Z')))

    def test_fogbugz_datetime_returns_20130221_2032380000_for_20130221T203238Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T20:32:38Z')))

    def test_fogbugz_datetime_returns_20130221_2032380000_for_20130221T203238Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T20:32:38Z')))

    def test_fogbugz_datetime_returns_20130221_2032380000_for_20130221T203238Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T20:32:38Z')))

    def test_fogbugz_datetime_returns_20130221_2130000000_for_20130221T213000Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T21:30:00Z')))

    def test_fogbugz_datetime_returns_20130221_2130000000_for_20130221T213000Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T21:30:00Z')))

    def test_fogbugz_datetime_returns_20130221_2130000000_for_20130221T213000Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T21:30:00Z')))

    def test_fogbugz_datetime_returns_20130221_2130000000_for_20130221T213000Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T21:30:00Z')))

    def test_fogbugz_datetime_returns_20130221_2146090000_for_20130221T214609Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T21:46:09Z')))

    def test_fogbugz_datetime_returns_20130221_2146090000_for_20130221T214609Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T21:46:09Z')))

    def test_fogbugz_datetime_returns_20130221_2146090000_for_20130221T214609Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T21:46:09Z')))

    def test_fogbugz_datetime_returns_20130221_2146090000_for_20130221T214609Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T21:46:09Z')))

    def test_fogbugz_datetime_returns_20130221_2236020000_for_20130221T223602Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T22:36:02Z')))

    def test_fogbugz_datetime_returns_20130221_2236020000_for_20130221T223602Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T22:36:02Z')))

    def test_fogbugz_datetime_returns_20130221_2300500000_for_20130221T230050Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T23:00:50Z')))

    def test_fogbugz_datetime_returns_20130221_2300500000_for_20130221T230050Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T23:00:50Z')))

    def test_fogbugz_datetime_returns_20130221_2302110000_for_20130221T230211Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T23:02:11Z')))

    def test_fogbugz_datetime_returns_20130221_2302110000_for_20130221T230211Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T23:02:11Z')))

    def test_fogbugz_datetime_returns_20130221_2302110000_for_20130221T230211Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T23:02:11Z')))

    def test_fogbugz_datetime_returns_20130221_2302110000_for_20130221T230211Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T23:02:11Z')))

    def test_fogbugz_datetime_returns_20130221_2311080000_for_20130221T231108Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T23:11:08Z')))

    def test_fogbugz_datetime_returns_20130221_2311080000_for_20130221T231108Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T23:11:08Z')))

    def test_fogbugz_datetime_returns_20130221_2311080000_for_20130221T231108Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T23:11:08Z')))

    def test_fogbugz_datetime_returns_20130221_2311080000_for_20130221T231108Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T23:11:08Z')))

    def test_fogbugz_datetime_returns_20130221_2314570000_for_20130221T231457Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T23:14:57Z')))

    def test_fogbugz_datetime_returns_20130221_2314570000_for_20130221T231457Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T23:14:57Z')))

    def test_fogbugz_datetime_returns_20130221_2314570000_for_20130221T231457Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T23:14:57Z')))

    def test_fogbugz_datetime_returns_20130221_2314570000_for_20130221T231457Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-21T23:14:57Z')))

    def test_fogbugz_datetime_returns_20130222_0004110000_for_20130222T000411Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T00:04:11Z')))

    def test_fogbugz_datetime_returns_20130222_0004110000_for_20130222T000411Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T00:04:11Z')))

    def test_fogbugz_datetime_returns_20130222_0004270000_for_20130222T000427Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T00:04:27Z')))

    def test_fogbugz_datetime_returns_20130222_0004270000_for_20130222T000427Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T00:04:27Z')))

    def test_fogbugz_datetime_returns_20130222_0203300000_for_20130222T020330Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T02:03:30Z')))

    def test_fogbugz_datetime_returns_20130222_0203300000_for_20130222T020330Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T02:03:30Z')))

    def test_fogbugz_datetime_returns_20130222_0203300000_for_20130222T020330Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T02:03:30Z')))

    def test_fogbugz_datetime_returns_20130222_0203300000_for_20130222T020330Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T02:03:30Z')))

    def test_fogbugz_datetime_returns_20130222_0229260000_for_20130222T022926Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T02:29:26Z')))

    def test_fogbugz_datetime_returns_20130222_0229260000_for_20130222T022926Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T02:29:26Z')))

    def test_fogbugz_datetime_returns_20130222_0229260000_for_20130222T022926Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T02:29:26Z')))

    def test_fogbugz_datetime_returns_20130222_0229260000_for_20130222T022926Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T02:29:26Z')))

    def test_fogbugz_datetime_returns_20130222_0252300000_for_20130222T025230Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T02:52:30Z')))

    def test_fogbugz_datetime_returns_20130222_0252300000_for_20130222T025230Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T02:52:30Z')))

    def test_fogbugz_datetime_returns_20130222_1559000000_for_20130222T155900Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T15:59:00Z')))

    def test_fogbugz_datetime_returns_20130222_1559000000_for_20130222T155900Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T15:59:00Z')))

    def test_fogbugz_datetime_returns_20130222_1803000000_for_20130222T180300Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T18:03:00Z')))

    def test_fogbugz_datetime_returns_20130222_1803000000_for_20130222T180300Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T18:03:00Z')))

    def test_fogbugz_datetime_returns_20130222_1803000000_for_20130222T180300Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T18:03:00Z')))

    def test_fogbugz_datetime_returns_20130222_1803000000_for_20130222T180300Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T18:03:00Z')))

    def test_fogbugz_datetime_returns_20130222_1837000000_for_20130222T183700Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T18:37:00Z')))

    def test_fogbugz_datetime_returns_20130222_1837000000_for_20130222T183700Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T18:37:00Z')))

    def test_fogbugz_datetime_returns_20130222_1837000000_for_20130222T183700Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T18:37:00Z')))

    def test_fogbugz_datetime_returns_20130222_1837000000_for_20130222T183700Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T18:37:00Z')))

    def test_fogbugz_datetime_returns_20130222_1847000000_for_20130222T184700Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T18:47:00Z')))

    def test_fogbugz_datetime_returns_20130222_1847000000_for_20130222T184700Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T18:47:00Z')))

    def test_fogbugz_datetime_returns_20130222_1847000000_for_20130222T184700Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T18:47:00Z')))

    def test_fogbugz_datetime_returns_20130222_1847000000_for_20130222T184700Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T18:47:00Z')))

    def test_fogbugz_datetime_returns_20130222_2123000000_for_20130222T212300Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T21:23:00Z')))

    def test_fogbugz_datetime_returns_20130222_2123000000_for_20130222T212300Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T21:23:00Z')))

    def test_fogbugz_datetime_returns_20130222_2123000000_for_20130222T212300Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T21:23:00Z')))

    def test_fogbugz_datetime_returns_20130222_2123000000_for_20130222T212300Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T21:23:00Z')))

    def test_fogbugz_datetime_returns_20130222_2130000000_for_20130222T213000Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T21:30:00Z')))

    def test_fogbugz_datetime_returns_20130222_2130000000_for_20130222T213000Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T21:30:00Z')))

    def test_fogbugz_datetime_returns_20130222_2130000000_for_20130222T213000Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T21:30:00Z')))

    def test_fogbugz_datetime_returns_20130222_2130000000_for_20130222T213000Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T21:30:00Z')))

    def test_fogbugz_datetime_returns_20130222_2319000000_for_20130222T231900Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T23:19:00Z')))

    def test_fogbugz_datetime_returns_20130222_2319000000_for_20130222T231900Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T23:19:00Z')))

    def test_fogbugz_datetime_returns_20130222_2319000000_for_20130222T231900Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T23:19:00Z')))

    def test_fogbugz_datetime_returns_20130222_2319000000_for_20130222T231900Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T23:19:00Z')))

    def test_fogbugz_datetime_returns_20130222_2321000000_for_20130222T232100Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T23:21:00Z')))

    def test_fogbugz_datetime_returns_20130222_2321000000_for_20130222T232100Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T23:21:00Z')))

    def test_fogbugz_datetime_returns_20130222_2321000000_for_20130222T232100Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T23:21:00Z')))

    def test_fogbugz_datetime_returns_20130222_2321000000_for_20130222T232100Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T23:21:00Z')))

    def test_fogbugz_datetime_returns_20130222_2324000000_for_20130222T232400Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T23:24:00Z')))

    def test_fogbugz_datetime_returns_20130222_2324000000_for_20130222T232400Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T23:24:00Z')))

    def test_fogbugz_datetime_returns_20130222_2324260000_for_20130222T232426Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T23:24:26Z')))

    def test_fogbugz_datetime_returns_20130222_2324260000_for_20130222T232426Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T23:24:26Z')))

    def test_fogbugz_datetime_returns_20130222_2353030000_for_20130222T235303Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T23:53:03Z')))

    def test_fogbugz_datetime_returns_20130222_2353030000_for_20130222T235303Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-22T23:53:03Z')))

    def test_fogbugz_datetime_returns_20130223_0247000000_for_20130223T024700Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T02:47:00Z')))

    def test_fogbugz_datetime_returns_20130223_0247000000_for_20130223T024700Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T02:47:00Z')))

    def test_fogbugz_datetime_returns_20130223_0251000000_for_20130223T025100Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T02:51:00Z')))

    def test_fogbugz_datetime_returns_20130223_0251000000_for_20130223T025100Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T02:51:00Z')))

    def test_fogbugz_datetime_returns_20130223_0321540000_for_20130223T032154Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T03:21:54Z')))

    def test_fogbugz_datetime_returns_20130223_0321540000_for_20130223T032154Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T03:21:54Z')))

    def test_fogbugz_datetime_returns_20130223_0344000000_for_20130223T034400Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T03:44:00Z')))

    def test_fogbugz_datetime_returns_20130223_0344000000_for_20130223T034400Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T03:44:00Z')))

    def test_fogbugz_datetime_returns_20130223_0344000000_for_20130223T034400Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T03:44:00Z')))

    def test_fogbugz_datetime_returns_20130223_0344000000_for_20130223T034400Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T03:44:00Z')))

    def test_fogbugz_datetime_returns_20130223_0401180000_for_20130223T040118Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T04:01:18Z')))

    def test_fogbugz_datetime_returns_20130223_0401180000_for_20130223T040118Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T04:01:18Z')))

    def test_fogbugz_datetime_returns_20130223_0523000000_for_20130223T052300Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T05:23:00Z')))

    def test_fogbugz_datetime_returns_20130223_0523000000_for_20130223T052300Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T05:23:00Z')))

    def test_fogbugz_datetime_returns_20130223_0606030000_for_20130223T060603Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T06:06:03Z')))

    def test_fogbugz_datetime_returns_20130223_0606030000_for_20130223T060603Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T06:06:03Z')))

    def test_fogbugz_datetime_returns_20130223_0606130000_for_20130223T060613Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T06:06:13Z')))

    def test_fogbugz_datetime_returns_20130223_0606130000_for_20130223T060613Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T06:06:13Z')))

    def test_fogbugz_datetime_returns_20130223_0842000000_for_20130223T084200Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T08:42:00Z')))

    def test_fogbugz_datetime_returns_20130223_0842000000_for_20130223T084200Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T08:42:00Z')))

    def test_fogbugz_datetime_returns_20130223_0842000000_for_20130223T084200Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T08:42:00Z')))

    def test_fogbugz_datetime_returns_20130223_0842000000_for_20130223T084200Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T08:42:00Z')))

    def test_fogbugz_datetime_returns_20130223_0916000000_for_20130223T091600Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T09:16:00Z')))

    def test_fogbugz_datetime_returns_20130223_0916000000_for_20130223T091600Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T09:16:00Z')))

    def test_fogbugz_datetime_returns_20130223_0916000000_for_20130223T091600Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T09:16:00Z')))

    def test_fogbugz_datetime_returns_20130223_0916000000_for_20130223T091600Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T09:16:00Z')))

    def test_fogbugz_datetime_returns_20130223_0920410000_for_20130223T092041Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T09:20:41Z')))

    def test_fogbugz_datetime_returns_20130223_0920410000_for_20130223T092041Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T09:20:41Z')))

    def test_fogbugz_datetime_returns_20130223_1743000000_for_20130223T174300Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T17:43:00Z')))

    def test_fogbugz_datetime_returns_20130223_1743000000_for_20130223T174300Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T17:43:00Z')))

    def test_fogbugz_datetime_returns_20130223_1823510000_for_20130223T182351Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T18:23:51Z')))

    def test_fogbugz_datetime_returns_20130223_1823510000_for_20130223T182351Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T18:23:51Z')))

    def test_fogbugz_datetime_returns_20130223_1823510000_for_20130223T182351Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T18:23:51Z')))

    def test_fogbugz_datetime_returns_20130223_1823510000_for_20130223T182351Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T18:23:51Z')))

    def test_fogbugz_datetime_returns_20130223_1825160000_for_20130223T182516Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T18:25:16Z')))

    def test_fogbugz_datetime_returns_20130223_1825160000_for_20130223T182516Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T18:25:16Z')))

    def test_fogbugz_datetime_returns_20130223_1825160000_for_20130223T182516Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T18:25:16Z')))

    def test_fogbugz_datetime_returns_20130223_1825160000_for_20130223T182516Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T18:25:16Z')))

    def test_fogbugz_datetime_returns_20130223_1922040000_for_20130223T192204Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T19:22:04Z')))

    def test_fogbugz_datetime_returns_20130223_1922040000_for_20130223T192204Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T19:22:04Z')))

    def test_fogbugz_datetime_returns_20130223_1934180000_for_20130223T193418Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T19:34:18Z')))

    def test_fogbugz_datetime_returns_20130223_1934180000_for_20130223T193418Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-23T19:34:18Z')))

    def test_fogbugz_datetime_returns_20130224_0052310000_for_20130224T005231Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-24T00:52:31Z')))

    def test_fogbugz_datetime_returns_20130224_0052310000_for_20130224T005231Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-24T00:52:31Z')))

    def test_fogbugz_datetime_returns_20130224_0133460000_for_20130224T013346Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-24T01:33:46Z')))

    def test_fogbugz_datetime_returns_20130224_0133460000_for_20130224T013346Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-24T01:33:46Z')))

    def test_fogbugz_datetime_returns_20130224_0400060000_for_20130224T040006Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-24T04:00:06Z')))

    def test_fogbugz_datetime_returns_20130224_0400060000_for_20130224T040006Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-24T04:00:06Z')))

    def test_fogbugz_datetime_returns_20130224_1931160000_for_20130224T193116Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-24T19:31:16Z')))

    def test_fogbugz_datetime_returns_20130224_1931160000_for_20130224T193116Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-24T19:31:16Z')))

    def test_fogbugz_datetime_returns_20130224_2019390000_for_20130224T201939Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-24T20:19:39Z')))

    def test_fogbugz_datetime_returns_20130224_2019390000_for_20130224T201939Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-24T20:19:39Z')))

    def test_fogbugz_datetime_returns_20130224_2056000000_for_20130224T205600Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-24T20:56:00Z')))

    def test_fogbugz_datetime_returns_20130224_2056000000_for_20130224T205600Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-24T20:56:00Z')))

    def test_fogbugz_datetime_returns_20130225_0459000000_for_20130225T045900Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-25T04:59:00Z')))

    def test_fogbugz_datetime_returns_20130225_0459000000_for_20130225T045900Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-25T04:59:00Z')))

    def test_fogbugz_datetime_returns_20130225_0500000000_for_20130225T050000Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-25T05:00:00Z')))

    def test_fogbugz_datetime_returns_20130225_0500000000_for_20130225T050000Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-25T05:00:00Z')))

    def test_fogbugz_datetime_returns_20130225_0512000000_for_20130225T051200Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-25T05:12:00Z')))

    def test_fogbugz_datetime_returns_20130225_0512000000_for_20130225T051200Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-25T05:12:00Z')))

    def test_fogbugz_datetime_returns_20130225_0512460000_for_20130225T051246Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-25T05:12:46Z')))

    def test_fogbugz_datetime_returns_20130225_0512460000_for_20130225T051246Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-25T05:12:46Z')))

    def test_fogbugz_datetime_returns_20130225_0514540000_for_20130225T051454Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-25T05:14:54Z')))

    def test_fogbugz_datetime_returns_20130225_0514540000_for_20130225T051454Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-25T05:14:54Z')))

    def test_fogbugz_datetime_returns_20130225_0514540000_for_20130225T051454Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-25T05:14:54Z')))

    def test_fogbugz_datetime_returns_20130225_0514540000_for_20130225T051454Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-25T05:14:54Z')))

    def test_fogbugz_datetime_returns_20130225_0516250000_for_20130225T051625Z(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-25T05:16:25Z')))

    def test_fogbugz_datetime_returns_20130225_0516250000_for_20130225T051625Z_case_2(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-25T05:16:25Z')))

    def test_fogbugz_datetime_returns_20130225_0516250000_for_20130225T051625Z_case_3(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-25T05:16:25Z')))

    def test_fogbugz_datetime_returns_20130225_0516250000_for_20130225T051625Z_case_4(self):
        self.assertEqual(datetime, type(fogbugz_datetime('2013-02-25T05:16:25Z')))

    def test_fogbugz_datetime_returns_date_str_for_date_str_equal_None(self):
        self.assertEqual(None, fogbugz_datetime(None))

class TestInterval(unittest.TestCase):
    def test___str___returns_str_instance_after_creation_with_case_id_equal_765_and_deleted_equal_false_and_interval_id_equal_967_and_person_id_equal_2_and_time_interval_equal_20130221_1325000500__20130221_1331090500_and_title_equal_Planning(self):
        interval = Interval(967, 2, 765, BoundedTimeInterval(), False, 'Planning')
        self.assertEqual('<ID:967 Person:2 Case:765 2013-02-21 13:25:00-05:00 - 2013-02-21 13:31:09-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_765_and_deleted_equal_false_and_interval_id_equal_972_and_person_id_equal_2_and_time_interval_equal_20130221_1432300500__20130221_1532380500_and_title_equal_Planning(self):
        interval = Interval(972, 2, 765, BoundedTimeInterval(), False, 'Planning')
        self.assertEqual('<ID:972 Person:2 Case:765 2013-02-21 14:32:30-05:00 - 2013-02-21 15:32:38-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_766_and_deleted_equal_false_and_interval_id_equal_968_and_person_id_equal_2_and_time_interval_equal_20130221_1304000500__20130221_1325000500_and_title_equal_Email_and_social_networking(self):
        interval = Interval(968, 2, 766, BoundedTimeInterval(), False, 'Email and social networking')
        self.assertEqual('<ID:968 Person:2 Case:766 2013-02-21 13:04:00-05:00 - 2013-02-21 13:25:00-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_766_and_deleted_equal_false_and_interval_id_equal_974_and_person_id_equal_2_and_time_interval_equal_20130221_1630000500__20130221_1646090500_and_title_equal_Email_and_social_networking(self):
        interval = Interval(974, 2, 766, BoundedTimeInterval(), False, 'Email and social networking')
        self.assertEqual('<ID:974 Person:2 Case:766 2013-02-21 16:30:00-05:00 - 2013-02-21 16:46:09-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_766_and_deleted_equal_false_and_interval_id_equal_978_and_person_id_equal_2_and_time_interval_equal_20130221_1811080500__20130221_1814570500_and_title_equal_Email_and_social_networking(self):
        interval = Interval(978, 2, 766, BoundedTimeInterval(), False, 'Email and social networking')
        self.assertEqual('<ID:978 Person:2 Case:766 2013-02-21 18:11:08-05:00 - 2013-02-21 18:14:57-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_766_and_deleted_equal_false_and_interval_id_equal_981_and_person_id_equal_2_and_time_interval_equal_20130221_2103300500__20130221_2129260500_and_title_equal_Email_and_social_networking(self):
        interval = Interval(981, 2, 766, BoundedTimeInterval(), False, 'Email and social networking')
        self.assertEqual('<ID:981 Person:2 Case:766 2013-02-21 21:03:30-05:00 - 2013-02-21 21:29:26-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_767_and_deleted_equal_false_and_interval_id_equal_971_and_person_id_equal_2_and_time_interval_equal_20130221_1407160500__20130221_1432300500_and_title_equal_Computer_maintenance(self):
        interval = Interval(971, 2, 767, BoundedTimeInterval(), False, 'Computer maintenance')
        self.assertEqual('<ID:971 Person:2 Case:767 2013-02-21 14:07:16-05:00 - 2013-02-21 14:32:30-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_769_and_deleted_equal_false_and_interval_id_equal_969_and_person_id_equal_2_and_time_interval_equal_20130221_1331090500__20130221_1345410500_and_title_equal_Status_Meeting_14_Feb_2013(self):
        interval = Interval(969, 2, 769, BoundedTimeInterval(), False, 'Status Meeting (14 Feb 2013)')
        self.assertEqual('<ID:969 Person:2 Case:769 2013-02-21 13:31:09-05:00 - 2013-02-21 13:45:41-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_769_and_deleted_equal_false_and_interval_id_equal_970_and_person_id_equal_2_and_time_interval_equal_20130221_1346100500__20130221_1407160500_and_title_equal_Status_Meeting_14_Feb_2013(self):
        interval = Interval(970, 2, 769, BoundedTimeInterval(), False, 'Status Meeting (14 Feb 2013)')
        self.assertEqual('<ID:970 Person:2 Case:769 2013-02-21 13:46:10-05:00 - 2013-02-21 14:07:16-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_805_and_deleted_equal_false_and_interval_id_equal_964_and_person_id_equal_2_and_time_interval_equal_20130221_0000000500__20130221_0106500500_and_title_equal_Implement_pickler(self):
        interval = Interval(964, 2, 805, BoundedTimeInterval(), False, 'Implement pickler')
        self.assertEqual('<ID:964 Person:2 Case:805 2013-02-21 00:00:00-05:00 - 2013-02-21 01:06:50-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_806_and_deleted_equal_false_and_interval_id_equal_965_and_person_id_equal_2_and_time_interval_equal_20130221_0107030500__20130221_0525000500_and_title_equal_Implement_fogbugz_download(self):
        interval = Interval(965, 2, 806, BoundedTimeInterval(), False, 'Implement fogbugz download')
        self.assertEqual('<ID:965 Person:2 Case:806 2013-02-21 01:07:03-05:00 - 2013-02-21 05:25:00-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_807_and_deleted_equal_false_and_interval_id_equal_1001_and_person_id_equal_2_and_time_interval_equal_20130223_1325160500__20130223_1422040500_and_title_equal_Implement_facebook_upload(self):
        interval = Interval(1001, 2, 807, BoundedTimeInterval(), False, 'Implement facebook upload')
        self.assertEqual('<ID:1001 Person:2 Case:807 2013-02-23 13:25:16-05:00 - 2013-02-23 14:22:04-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_807_and_deleted_equal_false_and_interval_id_equal_1002_and_person_id_equal_2_and_time_interval_equal_20130223_1434180500__20130223_1952310500_and_title_equal_Implement_facebook_upload(self):
        interval = Interval(1002, 2, 807, BoundedTimeInterval(), False, 'Implement facebook upload')
        self.assertEqual('<ID:1002 Person:2 Case:807 2013-02-23 14:34:18-05:00 - 2013-02-23 19:52:31-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_807_and_deleted_equal_false_and_interval_id_equal_1003_and_person_id_equal_2_and_time_interval_equal_20130223_2033460500__20130223_2300060500_and_title_equal_Implement_facebook_upload(self):
        interval = Interval(1003, 2, 807, BoundedTimeInterval(), False, 'Implement facebook upload')
        self.assertEqual('<ID:1003 Person:2 Case:807 2013-02-23 20:33:46-05:00 - 2013-02-23 23:00:06-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_808_and_deleted_equal_false_and_interval_id_equal_966_and_person_id_equal_2_and_time_interval_equal_20130221_0525000500__20130221_0551060500_and_title_equal_Push_voluntary_tracker_to_github(self):
        interval = Interval(966, 2, 808, BoundedTimeInterval(), False, 'Push voluntary tracker to github')
        self.assertEqual('<ID:966 Person:2 Case:808 2013-02-21 05:25:00-05:00 - 2013-02-21 05:51:06-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_810_and_deleted_equal_false_and_interval_id_equal_973_and_person_id_equal_2_and_time_interval_equal_20130221_1532380500__20130221_1630000500_and_title_equal_Move_fogbugz_direct_stuff_into_a_module_logon_queries_etc(self):
        interval = Interval(973, 2, 810, BoundedTimeInterval(), False, 'Move fogbugz direct stuff into a module (logon, queries, etc.)')
        self.assertEqual('<ID:973 Person:2 Case:810 2013-02-21 15:32:38-05:00 - 2013-02-21 16:30:00-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_810_and_deleted_equal_false_and_interval_id_equal_975_and_person_id_equal_2_and_time_interval_equal_20130221_1646090500__20130221_1736020500_and_title_equal_Move_fogbugz_direct_stuff_into_a_module_logon_queries_etc(self):
        interval = Interval(975, 2, 810, BoundedTimeInterval(), False, 'Move fogbugz direct stuff into a module (logon, queries, etc.)')
        self.assertEqual('<ID:975 Person:2 Case:810 2013-02-21 16:46:09-05:00 - 2013-02-21 17:36:02-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_810_and_deleted_equal_false_and_interval_id_equal_976_and_person_id_equal_2_and_time_interval_equal_20130221_1800500500__20130221_1802110500_and_title_equal_Move_fogbugz_direct_stuff_into_a_module_logon_queries_etc(self):
        interval = Interval(976, 2, 810, BoundedTimeInterval(), False, 'Move fogbugz direct stuff into a module (logon, queries, etc.)')
        self.assertEqual('<ID:976 Person:2 Case:810 2013-02-21 18:00:50-05:00 - 2013-02-21 18:02:11-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_811_and_deleted_equal_false_and_interval_id_equal_980_and_person_id_equal_2_and_time_interval_equal_20130221_1904270500__20130221_2103300500_and_title_equal_Create_FogbugzCase_class(self):
        interval = Interval(980, 2, 811, BoundedTimeInterval(), False, 'Create FogbugzCase class')
        self.assertEqual('<ID:980 Person:2 Case:811 2013-02-21 19:04:27-05:00 - 2013-02-21 21:03:30-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_811_and_deleted_equal_false_and_interval_id_equal_982_and_person_id_equal_2_and_time_interval_equal_20130221_2129260500__20130221_2152300500_and_title_equal_Create_FogbugzCase_class(self):
        interval = Interval(982, 2, 811, BoundedTimeInterval(), False, 'Create FogbugzCase class')
        self.assertEqual('<ID:982 Person:2 Case:811 2013-02-21 21:29:26-05:00 - 2013-02-21 21:52:30-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_812_and_deleted_equal_false_and_interval_id_equal_994_and_person_id_equal_2_and_time_interval_equal_20130222_2244000500__20130222_2301180500_and_title_equal_Rename_to_fogzap_and_repurpose_to_being_a_fogbugz_command_line_uitl_that_has_as_one_of_its_functions_uploading_to_facebook(self):
        interval = Interval(994, 2, 812, BoundedTimeInterval(), False, 'Rename to fogzap and repurpose to being a fogbugz command line uitl that has as one of its functions uploading to facebook')
        self.assertEqual('<ID:994 Person:2 Case:812 2013-02-22 22:44:00-05:00 - 2013-02-22 23:01:18-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_813_and_deleted_equal_false_and_interval_id_equal_996_and_person_id_equal_2_and_time_interval_equal_20130223_0106130500__20130223_0342000500_and_title_equal_Implement_a_subcommand_interface_with_commands_CaseStats_unimplemented_and_UnsharedIntervals(self):
        interval = Interval(996, 2, 813, BoundedTimeInterval(), False, 'Implement a subcommand interface with commands CaseStats (unimplemented) and UnsharedIntervals')
        self.assertEqual('<ID:996 Person:2 Case:813 2013-02-23 01:06:13-05:00 - 2013-02-23 03:42:00-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_815_and_deleted_equal_false_and_interval_id_equal_977_and_person_id_equal_2_and_time_interval_equal_20130221_1802110500__20130221_1811080500_and_title_equal_Reimplement_fogbugz_2_fb_using_the_library(self):
        interval = Interval(977, 2, 815, BoundedTimeInterval(), False, 'Reimplement fogbugz_2_fb using the library')
        self.assertEqual('<ID:977 Person:2 Case:815 2013-02-21 18:02:11-05:00 - 2013-02-21 18:11:08-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_815_and_deleted_equal_false_and_interval_id_equal_979_and_person_id_equal_2_and_time_interval_equal_20130221_1814570500__20130221_1904110500_and_title_equal_Reimplement_fogbugz_2_fb_using_the_library(self):
        interval = Interval(979, 2, 815, BoundedTimeInterval(), False, 'Reimplement fogbugz_2_fb using the library')
        self.assertEqual('<ID:979 Person:2 Case:815 2013-02-21 18:14:57-05:00 - 2013-02-21 19:04:11-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_816_and_deleted_equal_false_and_interval_id_equal_1000_and_person_id_equal_2_and_time_interval_equal_20130223_1323510500__20130223_1325160500_and_title_equal_Add_foglibSessioncases_named_method(self):
        interval = Interval(1000, 2, 816, BoundedTimeInterval(), False, 'Add foglib.Session.cases_named method')
        self.assertEqual('<ID:1000 Person:2 Case:816 2013-02-23 13:23:51-05:00 - 2013-02-23 13:25:16-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_818_and_deleted_equal_false_and_interval_id_equal_991_and_person_id_equal_2_and_time_interval_equal_20130222_1630000500__20130222_1819000500_and_title_equal_Meeting_with_Sriram_N(self):
        interval = Interval(991, 2, 818, BoundedTimeInterval(), False, 'Meeting with Sriram N.')
        self.assertEqual('<ID:991 Person:2 Case:818 2013-02-22 16:30:00-05:00 - 2013-02-22 18:19:00-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_819_and_deleted_equal_false_and_interval_id_equal_986_and_person_id_equal_2_and_time_interval_equal_20130222_1059000500__20130222_1303000500_and_title_equal_Sriram_N_job_talk(self):
        interval = Interval(986, 2, 819, BoundedTimeInterval(), False, 'Sriram N job talk')
        self.assertEqual('<ID:986 Person:2 Case:819 2013-02-22 10:59:00-05:00 - 2013-02-22 13:03:00-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_820_and_deleted_equal_false_and_interval_id_equal_1004_and_person_id_equal_2_and_time_interval_equal_20130224_1431160500__20130224_1519390500_and_title_equal_Email_and_social_networking(self):
        interval = Interval(1004, 2, 820, BoundedTimeInterval(), False, 'Email and social networking')
        self.assertEqual('<ID:1004 Person:2 Case:820 2013-02-24 14:31:16-05:00 - 2013-02-24 15:19:39-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_820_and_deleted_equal_false_and_interval_id_equal_983_and_person_id_equal_2_and_time_interval_equal_20130222_1824260500__20130222_1853030500_and_title_equal_Email_and_social_networking(self):
        interval = Interval(983, 2, 820, BoundedTimeInterval(), False, 'Email and social networking')
        self.assertEqual('<ID:983 Person:2 Case:820 2013-02-22 18:24:26-05:00 - 2013-02-22 18:53:03-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_820_and_deleted_equal_false_and_interval_id_equal_992_and_person_id_equal_2_and_time_interval_equal_20130222_1819000500__20130222_1821000500_and_title_equal_Email_and_social_networking(self):
        interval = Interval(992, 2, 820, BoundedTimeInterval(), False, 'Email and social networking')
        self.assertEqual('<ID:992 Person:2 Case:820 2013-02-22 18:19:00-05:00 - 2013-02-22 18:21:00-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_820_and_deleted_equal_false_and_interval_id_equal_999_and_person_id_equal_2_and_time_interval_equal_20130223_1243000500__20130223_1323510500_and_title_equal_Email_and_social_networking(self):
        interval = Interval(999, 2, 820, BoundedTimeInterval(), False, 'Email and social networking')
        self.assertEqual('<ID:999 Person:2 Case:820 2013-02-23 12:43:00-05:00 - 2013-02-23 13:23:51-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_821_and_deleted_equal_false_and_interval_id_equal_1008_and_person_id_equal_2_and_time_interval_equal_20130225_0014540500__20130225_0016250500_and_title_equal_Planning(self):
        interval = Interval(1008, 2, 821, BoundedTimeInterval(), False, 'Planning')
        self.assertEqual('<ID:1008 Person:2 Case:821 2013-02-25 00:14:54-05:00 - 2013-02-25 00:16:25-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_821_and_deleted_equal_false_and_interval_id_equal_984_and_person_id_equal_2_and_time_interval_equal_20130222_2147000500__20130222_2151000500_and_title_equal_Planning(self):
        interval = Interval(984, 2, 821, BoundedTimeInterval(), False, 'Planning')
        self.assertEqual('<ID:984 Person:2 Case:821 2013-02-22 21:47:00-05:00 - 2013-02-22 21:51:00-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_821_and_deleted_equal_false_and_interval_id_equal_985_and_person_id_equal_2_and_time_interval_equal_20130222_2221540500__20130222_2244000500_and_title_equal_Planning(self):
        interval = Interval(985, 2, 821, BoundedTimeInterval(), False, 'Planning')
        self.assertEqual('<ID:985 Person:2 Case:821 2013-02-22 22:21:54-05:00 - 2013-02-22 22:44:00-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_821_and_deleted_equal_false_and_interval_id_equal_988_and_person_id_equal_2_and_time_interval_equal_20130222_1337000500__20130222_1347000500_and_title_equal_Planning(self):
        interval = Interval(988, 2, 821, BoundedTimeInterval(), False, 'Planning')
        self.assertEqual('<ID:988 Person:2 Case:821 2013-02-22 13:37:00-05:00 - 2013-02-22 13:47:00-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_821_and_deleted_equal_false_and_interval_id_equal_990_and_person_id_equal_2_and_time_interval_equal_20130222_1623000500__20130222_1630000500_and_title_equal_Planning(self):
        interval = Interval(990, 2, 821, BoundedTimeInterval(), False, 'Planning')
        self.assertEqual('<ID:990 Person:2 Case:821 2013-02-22 16:23:00-05:00 - 2013-02-22 16:30:00-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_821_and_deleted_equal_false_and_interval_id_equal_993_and_person_id_equal_2_and_time_interval_equal_20130222_1821000500__20130222_1824000500_and_title_equal_Planning(self):
        interval = Interval(993, 2, 821, BoundedTimeInterval(), False, 'Planning')
        self.assertEqual('<ID:993 Person:2 Case:821 2013-02-22 18:21:00-05:00 - 2013-02-22 18:24:00-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_821_and_deleted_equal_false_and_interval_id_equal_998_and_person_id_equal_2_and_time_interval_equal_20130223_0416000500__20130223_0420410500_and_title_equal_Planning(self):
        interval = Interval(998, 2, 821, BoundedTimeInterval(), False, 'Planning')
        self.assertEqual('<ID:998 Person:2 Case:821 2013-02-23 04:16:00-05:00 - 2013-02-23 04:20:41-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_822_and_deleted_equal_false_and_interval_id_equal_987_and_person_id_equal_2_and_time_interval_equal_20130222_1303000500__20130222_1337000500_and_title_equal_Talk_with_coworkers(self):
        interval = Interval(987, 2, 822, BoundedTimeInterval(), False, 'Talk with co-workers')
        self.assertEqual('<ID:987 Person:2 Case:822 2013-02-22 13:03:00-05:00 - 2013-02-22 13:37:00-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_822_and_deleted_equal_false_and_interval_id_equal_989_and_person_id_equal_2_and_time_interval_equal_20130222_1347000500__20130222_1623000500_and_title_equal_Talk_with_coworkers(self):
        interval = Interval(989, 2, 822, BoundedTimeInterval(), False, 'Talk with co-workers')
        self.assertEqual('<ID:989 Person:2 Case:822 2013-02-22 13:47:00-05:00 - 2013-02-22 16:23:00-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_823_and_deleted_equal_false_and_interval_id_equal_995_and_person_id_equal_2_and_time_interval_equal_20130223_0023000500__20130223_0106030500_and_title_equal_Move_config_file_reading_to_its_own_file(self):
        interval = Interval(995, 2, 823, BoundedTimeInterval(), False, 'Move config file reading to its own file')
        self.assertEqual('<ID:995 Person:2 Case:823 2013-02-23 00:23:00-05:00 - 2013-02-23 01:06:03-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_824_and_deleted_equal_false_and_interval_id_equal_997_and_person_id_equal_2_and_time_interval_equal_20130223_0342000500__20130223_0416000500_and_title_equal_Implement_list_of_time_worked_for_each_unuploaded_day(self):
        interval = Interval(997, 2, 824, BoundedTimeInterval(), False, 'Implement list of time worked for each un-uploaded day')
        self.assertEqual('<ID:997 Person:2 Case:824 2013-02-23 03:42:00-05:00 - 2013-02-23 04:16:00-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_825_and_deleted_equal_false_and_interval_id_equal_1007_and_person_id_equal_2_and_time_interval_equal_20130225_0012460500__20130225_0014540500_and_title_equal_Add_test_cases_for_fogzap_and_libraries(self):
        interval = Interval(1007, 2, 825, BoundedTimeInterval(), False, 'Add test cases for fogzap and libraries')
        self.assertEqual('<ID:1007 Person:2 Case:825 2013-02-25 00:12:46-05:00 - 2013-02-25 00:14:54-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_825_and_deleted_equal_false_and_interval_id_equal_1009_and_person_id_equal_2_and_time_interval_equal_20130225_0016250500__Ongoing_and_title_equal_Add_test_cases_for_fogzap_and_libraries(self):
        interval = Interval(1009, 2, 825, OngoingTimeInterval(), False, 'Add test cases for fogzap and libraries')
        self.assertEqual('<ID:1009 Person:2 Case:825 2013-02-25 00:16:25-05:00 - Ongoing (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_826_and_deleted_equal_false_and_interval_id_equal_1005_and_person_id_equal_2_and_time_interval_equal_20130224_1556000500__20130224_2359000500_and_title_equal_Refactor_foglibInterval(self):
        interval = Interval(1005, 2, 826, BoundedTimeInterval(), False, 'Refactor foglib.Interval')
        self.assertEqual('<ID:1005 Person:2 Case:826 2013-02-24 15:56:00-05:00 - 2013-02-24 23:59:00-05:00 (not deleted)>', interval.__str__())

    def test___str___returns_str_instance_after_creation_with_case_id_equal_826_and_deleted_equal_false_and_interval_id_equal_1006_and_person_id_equal_2_and_time_interval_equal_20130225_0000000500__20130225_0012000500_and_title_equal_Refactor_foglibInterval(self):
        interval = Interval(1006, 2, 826, BoundedTimeInterval(), False, 'Refactor foglib.Interval')
        self.assertEqual('<ID:1006 Person:2 Case:826 2013-02-25 00:00:00-05:00 - 2013-02-25 00:12:00-05:00 (not deleted)>', interval.__str__())

    def test_creation_with_case_id_equal_765_and_deleted_equal_false_and_interval_id_equal_967_and_person_id_equal_2_and_time_interval_equal_20130221_1325000500__20130221_1331090500_and_title_equal_Planning(self):
        interval = Interval(967, 2, 765, BoundedTimeInterval(), False, 'Planning')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_765_and_deleted_equal_false_and_interval_id_equal_972_and_person_id_equal_2_and_time_interval_equal_20130221_1432300500__20130221_1532380500_and_title_equal_Planning(self):
        interval = Interval(972, 2, 765, BoundedTimeInterval(), False, 'Planning')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_766_and_deleted_equal_false_and_interval_id_equal_968_and_person_id_equal_2_and_time_interval_equal_20130221_1304000500__20130221_1325000500_and_title_equal_Email_and_social_networking(self):
        interval = Interval(968, 2, 766, BoundedTimeInterval(), False, 'Email and social networking')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_766_and_deleted_equal_false_and_interval_id_equal_974_and_person_id_equal_2_and_time_interval_equal_20130221_1630000500__20130221_1646090500_and_title_equal_Email_and_social_networking(self):
        interval = Interval(974, 2, 766, BoundedTimeInterval(), False, 'Email and social networking')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_766_and_deleted_equal_false_and_interval_id_equal_978_and_person_id_equal_2_and_time_interval_equal_20130221_1811080500__20130221_1814570500_and_title_equal_Email_and_social_networking(self):
        interval = Interval(978, 2, 766, BoundedTimeInterval(), False, 'Email and social networking')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_766_and_deleted_equal_false_and_interval_id_equal_981_and_person_id_equal_2_and_time_interval_equal_20130221_2103300500__20130221_2129260500_and_title_equal_Email_and_social_networking(self):
        interval = Interval(981, 2, 766, BoundedTimeInterval(), False, 'Email and social networking')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_767_and_deleted_equal_false_and_interval_id_equal_971_and_person_id_equal_2_and_time_interval_equal_20130221_1407160500__20130221_1432300500_and_title_equal_Computer_maintenance(self):
        interval = Interval(971, 2, 767, BoundedTimeInterval(), False, 'Computer maintenance')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_769_and_deleted_equal_false_and_interval_id_equal_969_and_person_id_equal_2_and_time_interval_equal_20130221_1331090500__20130221_1345410500_and_title_equal_Status_Meeting_14_Feb_2013(self):
        interval = Interval(969, 2, 769, BoundedTimeInterval(), False, 'Status Meeting (14 Feb 2013)')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_769_and_deleted_equal_false_and_interval_id_equal_970_and_person_id_equal_2_and_time_interval_equal_20130221_1346100500__20130221_1407160500_and_title_equal_Status_Meeting_14_Feb_2013(self):
        interval = Interval(970, 2, 769, BoundedTimeInterval(), False, 'Status Meeting (14 Feb 2013)')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_805_and_deleted_equal_false_and_interval_id_equal_964_and_person_id_equal_2_and_time_interval_equal_20130221_0000000500__20130221_0106500500_and_title_equal_Implement_pickler(self):
        interval = Interval(964, 2, 805, BoundedTimeInterval(), False, 'Implement pickler')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_806_and_deleted_equal_false_and_interval_id_equal_965_and_person_id_equal_2_and_time_interval_equal_20130221_0107030500__20130221_0525000500_and_title_equal_Implement_fogbugz_download(self):
        interval = Interval(965, 2, 806, BoundedTimeInterval(), False, 'Implement fogbugz download')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_807_and_deleted_equal_false_and_interval_id_equal_1001_and_person_id_equal_2_and_time_interval_equal_20130223_1325160500__20130223_1422040500_and_title_equal_Implement_facebook_upload(self):
        interval = Interval(1001, 2, 807, BoundedTimeInterval(), False, 'Implement facebook upload')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_807_and_deleted_equal_false_and_interval_id_equal_1002_and_person_id_equal_2_and_time_interval_equal_20130223_1434180500__20130223_1952310500_and_title_equal_Implement_facebook_upload(self):
        interval = Interval(1002, 2, 807, BoundedTimeInterval(), False, 'Implement facebook upload')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_807_and_deleted_equal_false_and_interval_id_equal_1003_and_person_id_equal_2_and_time_interval_equal_20130223_2033460500__20130223_2300060500_and_title_equal_Implement_facebook_upload(self):
        interval = Interval(1003, 2, 807, BoundedTimeInterval(), False, 'Implement facebook upload')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_808_and_deleted_equal_false_and_interval_id_equal_966_and_person_id_equal_2_and_time_interval_equal_20130221_0525000500__20130221_0551060500_and_title_equal_Push_voluntary_tracker_to_github(self):
        interval = Interval(966, 2, 808, BoundedTimeInterval(), False, 'Push voluntary tracker to github')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_810_and_deleted_equal_false_and_interval_id_equal_973_and_person_id_equal_2_and_time_interval_equal_20130221_1532380500__20130221_1630000500_and_title_equal_Move_fogbugz_direct_stuff_into_a_module_logon_queries_etc(self):
        interval = Interval(973, 2, 810, BoundedTimeInterval(), False, 'Move fogbugz direct stuff into a module (logon, queries, etc.)')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_810_and_deleted_equal_false_and_interval_id_equal_975_and_person_id_equal_2_and_time_interval_equal_20130221_1646090500__20130221_1736020500_and_title_equal_Move_fogbugz_direct_stuff_into_a_module_logon_queries_etc(self):
        interval = Interval(975, 2, 810, BoundedTimeInterval(), False, 'Move fogbugz direct stuff into a module (logon, queries, etc.)')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_810_and_deleted_equal_false_and_interval_id_equal_976_and_person_id_equal_2_and_time_interval_equal_20130221_1800500500__20130221_1802110500_and_title_equal_Move_fogbugz_direct_stuff_into_a_module_logon_queries_etc(self):
        interval = Interval(976, 2, 810, BoundedTimeInterval(), False, 'Move fogbugz direct stuff into a module (logon, queries, etc.)')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_811_and_deleted_equal_false_and_interval_id_equal_980_and_person_id_equal_2_and_time_interval_equal_20130221_1904270500__20130221_2103300500_and_title_equal_Create_FogbugzCase_class(self):
        interval = Interval(980, 2, 811, BoundedTimeInterval(), False, 'Create FogbugzCase class')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_811_and_deleted_equal_false_and_interval_id_equal_982_and_person_id_equal_2_and_time_interval_equal_20130221_2129260500__20130221_2152300500_and_title_equal_Create_FogbugzCase_class(self):
        interval = Interval(982, 2, 811, BoundedTimeInterval(), False, 'Create FogbugzCase class')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_812_and_deleted_equal_false_and_interval_id_equal_994_and_person_id_equal_2_and_time_interval_equal_20130222_2244000500__20130222_2301180500_and_title_equal_Rename_to_fogzap_and_repurpose_to_being_a_fogbugz_command_line_uitl_that_has_as_one_of_its_functions_uploading_to_facebook(self):
        interval = Interval(994, 2, 812, BoundedTimeInterval(), False, 'Rename to fogzap and repurpose to being a fogbugz command line uitl that has as one of its functions uploading to facebook')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_813_and_deleted_equal_false_and_interval_id_equal_996_and_person_id_equal_2_and_time_interval_equal_20130223_0106130500__20130223_0342000500_and_title_equal_Implement_a_subcommand_interface_with_commands_CaseStats_unimplemented_and_UnsharedIntervals(self):
        interval = Interval(996, 2, 813, BoundedTimeInterval(), False, 'Implement a subcommand interface with commands CaseStats (unimplemented) and UnsharedIntervals')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_815_and_deleted_equal_false_and_interval_id_equal_977_and_person_id_equal_2_and_time_interval_equal_20130221_1802110500__20130221_1811080500_and_title_equal_Reimplement_fogbugz_2_fb_using_the_library(self):
        interval = Interval(977, 2, 815, BoundedTimeInterval(), False, 'Reimplement fogbugz_2_fb using the library')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_815_and_deleted_equal_false_and_interval_id_equal_979_and_person_id_equal_2_and_time_interval_equal_20130221_1814570500__20130221_1904110500_and_title_equal_Reimplement_fogbugz_2_fb_using_the_library(self):
        interval = Interval(979, 2, 815, BoundedTimeInterval(), False, 'Reimplement fogbugz_2_fb using the library')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_816_and_deleted_equal_false_and_interval_id_equal_1000_and_person_id_equal_2_and_time_interval_equal_20130223_1323510500__20130223_1325160500_and_title_equal_Add_foglibSessioncases_named_method(self):
        interval = Interval(1000, 2, 816, BoundedTimeInterval(), False, 'Add foglib.Session.cases_named method')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_818_and_deleted_equal_false_and_interval_id_equal_991_and_person_id_equal_2_and_time_interval_equal_20130222_1630000500__20130222_1819000500_and_title_equal_Meeting_with_Sriram_N(self):
        interval = Interval(991, 2, 818, BoundedTimeInterval(), False, 'Meeting with Sriram N.')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_819_and_deleted_equal_false_and_interval_id_equal_986_and_person_id_equal_2_and_time_interval_equal_20130222_1059000500__20130222_1303000500_and_title_equal_Sriram_N_job_talk(self):
        interval = Interval(986, 2, 819, BoundedTimeInterval(), False, 'Sriram N job talk')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_820_and_deleted_equal_false_and_interval_id_equal_1004_and_person_id_equal_2_and_time_interval_equal_20130224_1431160500__20130224_1519390500_and_title_equal_Email_and_social_networking(self):
        interval = Interval(1004, 2, 820, BoundedTimeInterval(), False, 'Email and social networking')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_820_and_deleted_equal_false_and_interval_id_equal_983_and_person_id_equal_2_and_time_interval_equal_20130222_1824260500__20130222_1853030500_and_title_equal_Email_and_social_networking(self):
        interval = Interval(983, 2, 820, BoundedTimeInterval(), False, 'Email and social networking')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_820_and_deleted_equal_false_and_interval_id_equal_992_and_person_id_equal_2_and_time_interval_equal_20130222_1819000500__20130222_1821000500_and_title_equal_Email_and_social_networking(self):
        interval = Interval(992, 2, 820, BoundedTimeInterval(), False, 'Email and social networking')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_820_and_deleted_equal_false_and_interval_id_equal_999_and_person_id_equal_2_and_time_interval_equal_20130223_1243000500__20130223_1323510500_and_title_equal_Email_and_social_networking(self):
        interval = Interval(999, 2, 820, BoundedTimeInterval(), False, 'Email and social networking')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_821_and_deleted_equal_false_and_interval_id_equal_1008_and_person_id_equal_2_and_time_interval_equal_20130225_0014540500__20130225_0016250500_and_title_equal_Planning(self):
        interval = Interval(1008, 2, 821, BoundedTimeInterval(), False, 'Planning')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_821_and_deleted_equal_false_and_interval_id_equal_984_and_person_id_equal_2_and_time_interval_equal_20130222_2147000500__20130222_2151000500_and_title_equal_Planning(self):
        interval = Interval(984, 2, 821, BoundedTimeInterval(), False, 'Planning')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_821_and_deleted_equal_false_and_interval_id_equal_985_and_person_id_equal_2_and_time_interval_equal_20130222_2221540500__20130222_2244000500_and_title_equal_Planning(self):
        interval = Interval(985, 2, 821, BoundedTimeInterval(), False, 'Planning')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_821_and_deleted_equal_false_and_interval_id_equal_988_and_person_id_equal_2_and_time_interval_equal_20130222_1337000500__20130222_1347000500_and_title_equal_Planning(self):
        interval = Interval(988, 2, 821, BoundedTimeInterval(), False, 'Planning')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_821_and_deleted_equal_false_and_interval_id_equal_990_and_person_id_equal_2_and_time_interval_equal_20130222_1623000500__20130222_1630000500_and_title_equal_Planning(self):
        interval = Interval(990, 2, 821, BoundedTimeInterval(), False, 'Planning')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_821_and_deleted_equal_false_and_interval_id_equal_993_and_person_id_equal_2_and_time_interval_equal_20130222_1821000500__20130222_1824000500_and_title_equal_Planning(self):
        interval = Interval(993, 2, 821, BoundedTimeInterval(), False, 'Planning')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_821_and_deleted_equal_false_and_interval_id_equal_998_and_person_id_equal_2_and_time_interval_equal_20130223_0416000500__20130223_0420410500_and_title_equal_Planning(self):
        interval = Interval(998, 2, 821, BoundedTimeInterval(), False, 'Planning')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_822_and_deleted_equal_false_and_interval_id_equal_987_and_person_id_equal_2_and_time_interval_equal_20130222_1303000500__20130222_1337000500_and_title_equal_Talk_with_coworkers(self):
        interval = Interval(987, 2, 822, BoundedTimeInterval(), False, 'Talk with co-workers')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_822_and_deleted_equal_false_and_interval_id_equal_989_and_person_id_equal_2_and_time_interval_equal_20130222_1347000500__20130222_1623000500_and_title_equal_Talk_with_coworkers(self):
        interval = Interval(989, 2, 822, BoundedTimeInterval(), False, 'Talk with co-workers')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_823_and_deleted_equal_false_and_interval_id_equal_995_and_person_id_equal_2_and_time_interval_equal_20130223_0023000500__20130223_0106030500_and_title_equal_Move_config_file_reading_to_its_own_file(self):
        interval = Interval(995, 2, 823, BoundedTimeInterval(), False, 'Move config file reading to its own file')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_824_and_deleted_equal_false_and_interval_id_equal_997_and_person_id_equal_2_and_time_interval_equal_20130223_0342000500__20130223_0416000500_and_title_equal_Implement_list_of_time_worked_for_each_unuploaded_day(self):
        interval = Interval(997, 2, 824, BoundedTimeInterval(), False, 'Implement list of time worked for each un-uploaded day')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_825_and_deleted_equal_false_and_interval_id_equal_1007_and_person_id_equal_2_and_time_interval_equal_20130225_0012460500__20130225_0014540500_and_title_equal_Add_test_cases_for_fogzap_and_libraries(self):
        interval = Interval(1007, 2, 825, BoundedTimeInterval(), False, 'Add test cases for fogzap and libraries')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_825_and_deleted_equal_false_and_interval_id_equal_1009_and_person_id_equal_2_and_time_interval_equal_20130225_0016250500__Ongoing_and_title_equal_Add_test_cases_for_fogzap_and_libraries(self):
        interval = Interval(1009, 2, 825, OngoingTimeInterval(), False, 'Add test cases for fogzap and libraries')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_826_and_deleted_equal_false_and_interval_id_equal_1005_and_person_id_equal_2_and_time_interval_equal_20130224_1556000500__20130224_2359000500_and_title_equal_Refactor_foglibInterval(self):
        interval = Interval(1005, 2, 826, BoundedTimeInterval(), False, 'Refactor foglib.Interval')
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_case_id_equal_826_and_deleted_equal_false_and_interval_id_equal_1006_and_person_id_equal_2_and_time_interval_equal_20130225_0000000500__20130225_0012000500_and_title_equal_Refactor_foglibInterval(self):
        interval = Interval(1006, 2, 826, BoundedTimeInterval(), False, 'Refactor foglib.Interval')
        # Make sure it doesn't raise any exceptions.

    @unittest.expectedFailure
    def test_from_xml(self):
        # interval = Interval(interval_id, person_id, case_id, time_interval, deleted, title)
        # self.assertEqual(expected, interval.from_xml())
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here

class TestTimeInterval(unittest.TestCase):
    @unittest.expectedFailure
    def test___str__(self):
        # time_interval = TimeInterval()
        # self.assertEqual(expected, time_interval.__str__())
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here
class TestEmptyTimeInterval(unittest.TestCase):
    @unittest.expectedFailure
    def test___repr__(self):
        # empty_time_interval = EmptyTimeInterval()
        # self.assertEqual(expected, empty_time_interval.__repr__())
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here
    @unittest.expectedFailure
    def test_contains(self):
        # empty_time_interval = EmptyTimeInterval()
        # self.assertEqual(expected, empty_time_interval.contains(a_datetime))
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here
    @unittest.expectedFailure
    def test_duration(self):
        # empty_time_interval = EmptyTimeInterval()
        # self.assertEqual(expected, empty_time_interval.duration())
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here
    @unittest.expectedFailure
    def test_intersection_with(self):
        # empty_time_interval = EmptyTimeInterval()
        # self.assertEqual(expected, empty_time_interval.intersection_with(a_TimeInterval))
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here
    @unittest.expectedFailure
    def test_is_ongoing(self):
        # empty_time_interval = EmptyTimeInterval()
        # self.assertEqual(expected, empty_time_interval.is_ongoing())
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here
    @unittest.expectedFailure
    def test_subinterval_before(self):
        # empty_time_interval = EmptyTimeInterval()
        # self.assertEqual(expected, empty_time_interval.subinterval_before(a_datetime))
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here
    @unittest.expectedFailure
    def test_subinterval_starting_at_or_after(self):
        # empty_time_interval = EmptyTimeInterval()
        # self.assertEqual(expected, empty_time_interval.subinterval_starting_at_or_after(a_datetime))
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here
class TestBoundedTimeInterval(unittest.TestCase):
    @unittest.expectedFailure
    def test___new__(self):
        # bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here
    def test___repr___returns_20130221_0000000500__20130221_0106500500(self):
        first = datetime_from_19_char_string('20130221_0000000500')
        last  = datetime_from_19_char_string('20130221_0106500500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-21 00:00:00-05:00 - 2013-02-21 01:06:50-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130221_0107030500__20130221_0525000500(self):
        first = datetime_from_19_char_string('20130221_0107030500')
        last  = datetime_from_19_char_string('20130221_0525000500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-21 01:07:03-05:00 - 2013-02-21 05:25:00-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130221_0525000500__20130221_0551060500(self):
        first = datetime_from_19_char_string('20130221_0525000500')
        last  = datetime_from_19_char_string('20130221_0551060500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-21 05:25:00-05:00 - 2013-02-21 05:51:06-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130221_1304000500__20130221_1325000500(self):
        first = datetime_from_19_char_string('20130221_1304000500')
        last  = datetime_from_19_char_string('20130221_1325000500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-21 13:04:00-05:00 - 2013-02-21 13:25:00-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130221_1325000500__20130221_1331090500(self):
        first = datetime_from_19_char_string('20130221_1325000500')
        last  = datetime_from_19_char_string('20130221_1331090500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-21 13:25:00-05:00 - 2013-02-21 13:31:09-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130221_1331090500__20130221_1345410500(self):
        first = datetime_from_19_char_string('20130221_1331090500')
        last  = datetime_from_19_char_string('20130221_1345410500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-21 13:31:09-05:00 - 2013-02-21 13:45:41-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130221_1346100500__20130221_1407160500(self):
        first = datetime_from_19_char_string('20130221_1346100500')
        last  = datetime_from_19_char_string('20130221_1407160500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-21 13:46:10-05:00 - 2013-02-21 14:07:16-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130221_1407160500__20130221_1432300500(self):
        first = datetime_from_19_char_string('20130221_1407160500')
        last  = datetime_from_19_char_string('20130221_1432300500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-21 14:07:16-05:00 - 2013-02-21 14:32:30-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130221_1432300500__20130221_1532380500(self):
        first = datetime_from_19_char_string('20130221_1432300500')
        last  = datetime_from_19_char_string('20130221_1532380500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-21 14:32:30-05:00 - 2013-02-21 15:32:38-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130221_1532380500__20130221_1630000500(self):
        first = datetime_from_19_char_string('20130221_1532380500')
        last  = datetime_from_19_char_string('20130221_1630000500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-21 15:32:38-05:00 - 2013-02-21 16:30:00-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130221_1630000500__20130221_1646090500(self):
        first = datetime_from_19_char_string('20130221_1630000500')
        last  = datetime_from_19_char_string('20130221_1646090500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-21 16:30:00-05:00 - 2013-02-21 16:46:09-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130221_1646090500__20130221_1736020500(self):
        first = datetime_from_19_char_string('20130221_1646090500')
        last  = datetime_from_19_char_string('20130221_1736020500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-21 16:46:09-05:00 - 2013-02-21 17:36:02-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130221_1800500500__20130221_1802110500(self):
        first = datetime_from_19_char_string('20130221_1800500500')
        last  = datetime_from_19_char_string('20130221_1802110500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-21 18:00:50-05:00 - 2013-02-21 18:02:11-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130221_1802110500__20130221_1811080500(self):
        first = datetime_from_19_char_string('20130221_1802110500')
        last  = datetime_from_19_char_string('20130221_1811080500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-21 18:02:11-05:00 - 2013-02-21 18:11:08-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130221_1811080500__20130221_1814570500(self):
        first = datetime_from_19_char_string('20130221_1811080500')
        last  = datetime_from_19_char_string('20130221_1814570500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-21 18:11:08-05:00 - 2013-02-21 18:14:57-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130221_1814570500__20130221_1904110500(self):
        first = datetime_from_19_char_string('20130221_1814570500')
        last  = datetime_from_19_char_string('20130221_1904110500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-21 18:14:57-05:00 - 2013-02-21 19:04:11-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130221_1904270500__20130221_2103300500(self):
        first = datetime_from_19_char_string('20130221_1904270500')
        last  = datetime_from_19_char_string('20130221_2103300500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-21 19:04:27-05:00 - 2013-02-21 21:03:30-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130221_2103300500__20130221_2129260500(self):
        first = datetime_from_19_char_string('20130221_2103300500')
        last  = datetime_from_19_char_string('20130221_2129260500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-21 21:03:30-05:00 - 2013-02-21 21:29:26-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130221_2129260500__20130221_2152300500(self):
        first = datetime_from_19_char_string('20130221_2129260500')
        last  = datetime_from_19_char_string('20130221_2152300500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-21 21:29:26-05:00 - 2013-02-21 21:52:30-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130222_1059000500__20130222_1303000500(self):
        first = datetime_from_19_char_string('20130222_1059000500')
        last  = datetime_from_19_char_string('20130222_1303000500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-22 10:59:00-05:00 - 2013-02-22 13:03:00-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130222_1303000500__20130222_1337000500(self):
        first = datetime_from_19_char_string('20130222_1303000500')
        last  = datetime_from_19_char_string('20130222_1337000500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-22 13:03:00-05:00 - 2013-02-22 13:37:00-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130222_1337000500__20130222_1347000500(self):
        first = datetime_from_19_char_string('20130222_1337000500')
        last  = datetime_from_19_char_string('20130222_1347000500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-22 13:37:00-05:00 - 2013-02-22 13:47:00-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130222_1347000500__20130222_1623000500(self):
        first = datetime_from_19_char_string('20130222_1347000500')
        last  = datetime_from_19_char_string('20130222_1623000500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-22 13:47:00-05:00 - 2013-02-22 16:23:00-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130222_1623000500__20130222_1630000500(self):
        first = datetime_from_19_char_string('20130222_1623000500')
        last  = datetime_from_19_char_string('20130222_1630000500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-22 16:23:00-05:00 - 2013-02-22 16:30:00-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130222_1630000500__20130222_1819000500(self):
        first = datetime_from_19_char_string('20130222_1630000500')
        last  = datetime_from_19_char_string('20130222_1819000500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-22 16:30:00-05:00 - 2013-02-22 18:19:00-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130222_1819000500__20130222_1821000500(self):
        first = datetime_from_19_char_string('20130222_1819000500')
        last  = datetime_from_19_char_string('20130222_1821000500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-22 18:19:00-05:00 - 2013-02-22 18:21:00-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130222_1821000500__20130222_1824000500(self):
        first = datetime_from_19_char_string('20130222_1821000500')
        last  = datetime_from_19_char_string('20130222_1824000500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-22 18:21:00-05:00 - 2013-02-22 18:24:00-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130222_1824260500__20130222_1853030500(self):
        first = datetime_from_19_char_string('20130222_1824260500')
        last  = datetime_from_19_char_string('20130222_1853030500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-22 18:24:26-05:00 - 2013-02-22 18:53:03-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130222_2147000500__20130222_2151000500(self):
        first = datetime_from_19_char_string('20130222_2147000500')
        last  = datetime_from_19_char_string('20130222_2151000500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-22 21:47:00-05:00 - 2013-02-22 21:51:00-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130222_2221540500__20130222_2244000500(self):
        first = datetime_from_19_char_string('20130222_2221540500')
        last  = datetime_from_19_char_string('20130222_2244000500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-22 22:21:54-05:00 - 2013-02-22 22:44:00-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130222_2244000500__20130222_2301180500(self):
        first = datetime_from_19_char_string('20130222_2244000500')
        last  = datetime_from_19_char_string('20130222_2301180500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-22 22:44:00-05:00 - 2013-02-22 23:01:18-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130223_0023000500__20130223_0106030500(self):
        first = datetime_from_19_char_string('20130223_0023000500')
        last  = datetime_from_19_char_string('20130223_0106030500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-23 00:23:00-05:00 - 2013-02-23 01:06:03-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130223_0106130500__20130223_0342000500(self):
        first = datetime_from_19_char_string('20130223_0106130500')
        last  = datetime_from_19_char_string('20130223_0342000500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-23 01:06:13-05:00 - 2013-02-23 03:42:00-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130223_0342000500__20130223_0416000500(self):
        first = datetime_from_19_char_string('20130223_0342000500')
        last  = datetime_from_19_char_string('20130223_0416000500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-23 03:42:00-05:00 - 2013-02-23 04:16:00-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130223_0416000500__20130223_0420410500(self):
        first = datetime_from_19_char_string('20130223_0416000500')
        last  = datetime_from_19_char_string('20130223_0420410500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-23 04:16:00-05:00 - 2013-02-23 04:20:41-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130223_1243000500__20130223_1323510500(self):
        first = datetime_from_19_char_string('20130223_1243000500')
        last  = datetime_from_19_char_string('20130223_1323510500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-23 12:43:00-05:00 - 2013-02-23 13:23:51-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130223_1323510500__20130223_1325160500(self):
        first = datetime_from_19_char_string('20130223_1323510500')
        last  = datetime_from_19_char_string('20130223_1325160500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-23 13:23:51-05:00 - 2013-02-23 13:25:16-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130223_1325160500__20130223_1422040500(self):
        first = datetime_from_19_char_string('20130223_1325160500')
        last  = datetime_from_19_char_string('20130223_1422040500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-23 13:25:16-05:00 - 2013-02-23 14:22:04-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130223_1434180500__20130223_1952310500(self):
        first = datetime_from_19_char_string('20130223_1434180500')
        last  = datetime_from_19_char_string('20130223_1952310500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-23 14:34:18-05:00 - 2013-02-23 19:52:31-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130223_2033460500__20130223_2300060500(self):
        first = datetime_from_19_char_string('20130223_2033460500')
        last  = datetime_from_19_char_string('20130223_2300060500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-23 20:33:46-05:00 - 2013-02-23 23:00:06-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130224_1431160500__20130224_1519390500(self):
        first = datetime_from_19_char_string('20130224_1431160500')
        last  = datetime_from_19_char_string('20130224_1519390500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-24 14:31:16-05:00 - 2013-02-24 15:19:39-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130224_1556000500__20130224_2359000500(self):
        first = datetime_from_19_char_string('20130224_1556000500')
        last  = datetime_from_19_char_string('20130224_2359000500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-24 15:56:00-05:00 - 2013-02-24 23:59:00-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130225_0000000500__20130225_0012000500(self):
        first = datetime_from_19_char_string('20130225_0000000500')
        last  = datetime_from_19_char_string('20130225_0012000500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-25 00:00:00-05:00 - 2013-02-25 00:12:00-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130225_0012460500__20130225_0014540500(self):
        first = datetime_from_19_char_string('20130225_0012460500')
        last  = datetime_from_19_char_string('20130225_0014540500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-25 00:12:46-05:00 - 2013-02-25 00:14:54-05:00', bounded_time_interval.__repr__())

    def test___repr___returns_20130225_0014540500__20130225_0016250500(self):
        first = datetime_from_19_char_string('20130225_0014540500')
        last  = datetime_from_19_char_string('20130225_0016250500')
        bounded_time_interval = BoundedTimeInterval(first, last)
        self.assertEqual('2013-02-25 00:14:54-05:00 - 2013-02-25 00:16:25-05:00', bounded_time_interval.__repr__())

    @unittest.expectedFailure
    def test_contains(self):
        # bounded_time_interval = BoundedTimeInterval(first, last)
        # self.assertEqual(expected, bounded_time_interval.contains(a_datetime))
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here
    @unittest.expectedFailure
    def test_duration(self):
        # bounded_time_interval = BoundedTimeInterval(first, last)
        # self.assertEqual(expected, bounded_time_interval.duration())
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here
    def test_intersection_with_and_is_ongoing(self):
        bounded_time_interval = BoundedTimeInterval()
        self.assertEqual(False, bounded_time_interval.is_ongoing())
        self.assertRaises(AttributeError, lambda: bounded_time_interval.intersection_with(BoundedTimeInterval()))


    def test_intersection_with_raises_attribute_error_for_20130225_0000000500__20130225_2359599999990500(self):
        bounded_time_interval = BoundedTimeInterval()
        self.assertRaises(AttributeError, lambda: bounded_time_interval.intersection_with(BoundedTimeInterval()))

    def test_is_ongoing_returns_false(self):
        bounded_time_interval = BoundedTimeInterval()
        self.assertEqual(False, bounded_time_interval.is_ongoing())


    @unittest.expectedFailure
    def test_subinterval_before(self):
        # bounded_time_interval = BoundedTimeInterval(first, last)
        # self.assertEqual(expected, bounded_time_interval.subinterval_before(a_datetime))
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here
    @unittest.expectedFailure
    def test_subinterval_starting_at_or_after(self):
        # bounded_time_interval = BoundedTimeInterval(first, last)
        # self.assertEqual(expected, bounded_time_interval.subinterval_starting_at_or_after(a_datetime))
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here
class TestOngoingTimeInterval(unittest.TestCase):
    @unittest.expectedFailure
    def test___new__(self):
        # ongoing_time_interval = OngoingTimeInterval(first)
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here
    def test___repr___returns_20130225_0016250500__Ongoing(self):
        ongoing_time_interval = OngoingTimeInterval()
        self.assertEqual('2013-02-25 00:16:25-05:00 - Ongoing', ongoing_time_interval.__repr__())

    @unittest.expectedFailure
    def test_contains(self):
        # ongoing_time_interval = OngoingTimeInterval(first)
        # self.assertEqual(expected, ongoing_time_interval.contains(a_datetime))
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here
    @unittest.expectedFailure
    def test_intersection_with(self):
        # ongoing_time_interval = OngoingTimeInterval(first)
        # self.assertEqual(expected, ongoing_time_interval.intersection_with(a_TimeInterval))
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here
    def test_is_ongoing_returns_true(self):
        ongoing_time_interval = OngoingTimeInterval()
        self.assertEqual(True, ongoing_time_interval.is_ongoing())

    @unittest.expectedFailure
    def test_subinterval_before(self):
        # ongoing_time_interval = OngoingTimeInterval(first)
        # self.assertEqual(expected, ongoing_time_interval.subinterval_before(a_datetime))
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here
    @unittest.expectedFailure
    def test_subinterval_starting_at_or_after(self):
        # ongoing_time_interval = OngoingTimeInterval(first)
        # self.assertEqual(expected, ongoing_time_interval.subinterval_starting_at_or_after(a_datetime))
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here
class TestIncompatibleAPIVersionException(unittest.TestCase):
    @unittest.expectedFailure
    def test___init__(self):
        # incompatible_api_version_exception = IncompatibleAPIVersionException(api_min_ver, api_supp_ver)
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here
class TestCaseAttribute(unittest.TestCase):
    @unittest.expectedFailure
    def test___init__(self):
        # case_attribute = CaseAttribute(name, sample_data, description)
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here
    @unittest.expectedFailure
    def test_all(self):
        # case_attribute = CaseAttribute(name, sample_data, description)
        # self.assertEqual(expected, case_attribute.all())
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here
    @unittest.expectedFailure
    def test_from_name(self):
        # case_attribute = CaseAttribute(name, sample_data, description)
        # self.assertEqual(expected, case_attribute.from_name(name))
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here
class TestUnparsedCaseValue(unittest.TestCase):
    @unittest.expectedFailure
    def test___init__(self):
        # unparsed_case_value = UnparsedCaseValue(attribute, text)
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here
class TestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test___init__(self):
        # case = Case(root)
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here
class TestLoginException(unittest.TestCase):
    @unittest.expectedFailure
    def test___init__(self):
        # login_exception = LoginException(xml)
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here
class TestSession(unittest.TestCase):
    @unittest.expectedFailure
    def test_isLoggedIn(self):
        # session = Session()
        # self.assertEqual(expected, session.isLoggedIn())
        self.assertTrue(False, "Haven't implemented this test yet") 
        # TODO: implement your test here
if __name__ == '__main__':
    unittest.main()
