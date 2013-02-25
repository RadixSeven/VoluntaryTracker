from foglib import fogbugz_datetime
import types
import unittest
from foglib import Interval
from foglib import BoundedTimeInterval
from foglib import OngoingTimeInterval
from foglib import Session
from fogzap import read_configuration_variables
from fogzap import time_interval_for_day_containing
from fogzap import split_into_days
from fogzap import summarize_intervals_by_day
from fogzap import Command
from fogzap import list_unshared_intervals
from fogzap import list_unshared_work_times
from fogzap import CommandWithoutLogin
from fogzap import list_commands
from fogzap import run_fogzap


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



class TestReadConfigurationVariables(unittest.TestCase):
    def test_read_configuration_variables_returns_tuple(self):
        self.assertEqual(tuple, type(read_configuration_variables()))

    def test_read_configuration_variables_returns_tuple_case_2(self):
        self.assertEqual(tuple, type(read_configuration_variables()))

    def test_read_configuration_variables_returns_tuple_case_3(self):
        self.assertEqual(tuple, type(read_configuration_variables()))

class TestTimeIntervalForDayContaining(unittest.TestCase):
    def test_time_interval_for_day_containing_returns_20130221_0000000500__20130221_2359599999990500_for_a_datetime_equal_20130221_0106500500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130221_0000000500__20130221_2359599999990500_for_a_datetime_equal_20130221_0525000500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130221_0000000500__20130221_2359599999990500_for_a_datetime_equal_20130221_0551060500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130221_0000000500__20130221_2359599999990500_for_a_datetime_equal_20130221_1325000500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130221_0000000500__20130221_2359599999990500_for_a_datetime_equal_20130221_1331090500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130221_0000000500__20130221_2359599999990500_for_a_datetime_equal_20130221_1345410500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130221_0000000500__20130221_2359599999990500_for_a_datetime_equal_20130221_1407160500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130221_0000000500__20130221_2359599999990500_for_a_datetime_equal_20130221_1432300500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130221_0000000500__20130221_2359599999990500_for_a_datetime_equal_20130221_1532380500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130221_0000000500__20130221_2359599999990500_for_a_datetime_equal_20130221_1630000500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130221_0000000500__20130221_2359599999990500_for_a_datetime_equal_20130221_1646090500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130221_0000000500__20130221_2359599999990500_for_a_datetime_equal_20130221_1736020500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130221_0000000500__20130221_2359599999990500_for_a_datetime_equal_20130221_1802110500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130221_0000000500__20130221_2359599999990500_for_a_datetime_equal_20130221_1811080500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130221_0000000500__20130221_2359599999990500_for_a_datetime_equal_20130221_1814570500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130221_0000000500__20130221_2359599999990500_for_a_datetime_equal_20130221_1904110500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130221_0000000500__20130221_2359599999990500_for_a_datetime_equal_20130221_2103300500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130221_0000000500__20130221_2359599999990500_for_a_datetime_equal_20130221_2129260500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130221_0000000500__20130221_2359599999990500_for_a_datetime_equal_20130221_2152300500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130222_0000000500__20130222_2359599999990500_for_a_datetime_equal_20130222_1303000500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130222_0000000500__20130222_2359599999990500_for_a_datetime_equal_20130222_1337000500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130222_0000000500__20130222_2359599999990500_for_a_datetime_equal_20130222_1347000500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130222_0000000500__20130222_2359599999990500_for_a_datetime_equal_20130222_1623000500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130222_0000000500__20130222_2359599999990500_for_a_datetime_equal_20130222_1630000500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130222_0000000500__20130222_2359599999990500_for_a_datetime_equal_20130222_1819000500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130222_0000000500__20130222_2359599999990500_for_a_datetime_equal_20130222_1821000500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130222_0000000500__20130222_2359599999990500_for_a_datetime_equal_20130222_1824000500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130222_0000000500__20130222_2359599999990500_for_a_datetime_equal_20130222_1853030500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130222_0000000500__20130222_2359599999990500_for_a_datetime_equal_20130222_2151000500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130222_0000000500__20130222_2359599999990500_for_a_datetime_equal_20130222_2244000500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130222_0000000500__20130222_2359599999990500_for_a_datetime_equal_20130222_2301180500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130223_0000000500__20130223_2359599999990500_for_a_datetime_equal_20130223_0106030500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130223_0000000500__20130223_2359599999990500_for_a_datetime_equal_20130223_0342000500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130223_0000000500__20130223_2359599999990500_for_a_datetime_equal_20130223_0416000500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130223_0000000500__20130223_2359599999990500_for_a_datetime_equal_20130223_0420410500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130223_0000000500__20130223_2359599999990500_for_a_datetime_equal_20130223_1323510500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130223_0000000500__20130223_2359599999990500_for_a_datetime_equal_20130223_1325160500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130223_0000000500__20130223_2359599999990500_for_a_datetime_equal_20130223_1422040500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130223_0000000500__20130223_2359599999990500_for_a_datetime_equal_20130223_1952310500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130223_0000000500__20130223_2359599999990500_for_a_datetime_equal_20130223_2300060500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130224_0000000500__20130224_2359599999990500_for_a_datetime_equal_20130224_1519390500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130224_0000000500__20130224_2359599999990500_for_a_datetime_equal_20130224_2359000500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130225_0000000500__20130225_2359599999990500_for_a_datetime_equal_20130225_0012000500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130225_0000000500__20130225_2359599999990500_for_a_datetime_equal_20130225_0014540500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130225_0000000500__20130225_2359599999990500_for_a_datetime_equal_20130225_0016250500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

    def test_time_interval_for_day_containing_returns_20130225_0000000500__20130225_2359599999990500_for_a_datetime_equal_20130225_0123543397930500_and_a_timezone_equal_local_timezone_instance(self):
        # obj1 = <TODO: datetime.timedelta>
        # obj2 = <TODO: datetime.timedelta>
        # obj3 = <TODO: datetime.datetime>
        # self.assertEqual(BoundedTimeInterval(), time_interval_for_day_containing(<TODO: datetime.datetime>, LocalTimezone()))
        pass

class TestSplitIntoDays(unittest.TestCase):
    def test_split_into_days_returns_list_for_20130221_0000000500__20130221_0106500500(self):
        first = datetime_from_19_char_string('20130221_0000000500')
        last  = datetime_from_19_char_string('20130221_0106500500')
        to_split = BoundedTimeInterval(first, last)
        self.assertEqual([to_split], split_into_days(to_split))

    def test_split_into_days_returns_list_for_20130221_0107030500__20130221_0525000500(self):
        first = datetime_from_19_char_string('20130221_0107030500')
        last  = datetime_from_19_char_string('20130221_0525000500')
        to_split = BoundedTimeInterval(first, last)
        self.assertEqual([to_split], split_into_days(to_split))


class TestSummarizeIntervalsByDay(unittest.TestCase):
    def test_summarize_intervals_by_day_returns_dict_for_list(self):
        pass
#        self.assertEqual({}, summarize_intervals_by_day([Interval(964, 2, 805, BoundedTimeInterval(), False, 'Implement pickler'), Interval(965, 2, 806, BoundedTimeInterval(), False, 'Implement fogbugz download'), Interval(966, 2, 808, BoundedTimeInterval(), False, 'Push voluntary tracker to github'), Interval(968, 2, 766, BoundedTimeInterval(), False, 'Email and social networking'), Interval(967, 2, 765, BoundedTimeInterval(), False, 'Planning'), Interval(969, 2, 769, BoundedTimeInterval(), False, 'Status Meeting (14 Feb 2013)'), Interval(970, 2, 769, BoundedTimeInterval(), False, 'Status Meeting (14 Feb 2013)'), Interval(971, 2, 767, BoundedTimeInterval(), False, 'Computer maintenance'), Interval(972, 2, 765, BoundedTimeInterval(), False, 'Planning'), Interval(973, 2, 810, BoundedTimeInterval(), False, 'Move fogbugz direct stuff into a module (logon, queries, etc.)'), Interval(974, 2, 766, BoundedTimeInterval(), False, 'Email and social networking'), Interval(975, 2, 810, BoundedTimeInterval(), False, 'Move fogbugz direct stuff into a module (logon, queries, etc.)'), Interval(976, 2, 810, BoundedTimeInterval(), False, 'Move fogbugz direct stuff into a module (logon, queries, etc.)'), Interval(977, 2, 815, BoundedTimeInterval(), False, 'Reimplement fogbugz_2_fb using the library'), Interval(978, 2, 766, BoundedTimeInterval(), False, 'Email and social networking'), Interval(979, 2, 815, BoundedTimeInterval(), False, 'Reimplement fogbugz_2_fb using the library'), Interval(980, 2, 811, BoundedTimeInterval(), False, 'Create FogbugzCase class'), Interval(981, 2, 766, BoundedTimeInterval(), False, 'Email and social networking'), Interval(982, 2, 811, BoundedTimeInterval(), False, 'Create FogbugzCase class'), Interval(986, 2, 819, BoundedTimeInterval(), False, 'Sriram N job talk'), Interval(987, 2, 822, BoundedTimeInterval(), False, 'Talk with co-workers'), Interval(988, 2, 821, BoundedTimeInterval(), False, 'Planning'), Interval(989, 2, 822, BoundedTimeInterval(), False, 'Talk with co-workers'), Interval(990, 2, 821, BoundedTimeInterval(), False, 'Planning'), Interval(991, 2, 818, BoundedTimeInterval(), False, 'Meeting with Sriram N.'), Interval(992, 2, 820, BoundedTimeInterval(), False, 'Email and social networking'), Interval(993, 2, 821, BoundedTimeInterval(), False, 'Planning'), Interval(983, 2, 820, BoundedTimeInterval(), False, 'Email and social networking'), Interval(984, 2, 821, BoundedTimeInterval(), False, 'Planning'), Interval(985, 2, 821, BoundedTimeInterval(), False, 'Planning'), Interval(994, 2, 812, BoundedTimeInterval(), False, 'Rename to fogzap and repurpose to being a fogbugz command line uitl that has as one of its functions uploading to facebook'), Interval(995, 2, 823, BoundedTimeInterval(), False, 'Move config file reading to its own file'), Interval(996, 2, 813, BoundedTimeInterval(), False, 'Implement a subcommand interface with commands CaseStats (unimplemented) and UnsharedIntervals'), Interval(997, 2, 824, BoundedTimeInterval(), False, 'Implement list of time worked for each un-uploaded day'), Interval(998, 2, 821, BoundedTimeInterval(), False, 'Planning'), Interval(999, 2, 820, BoundedTimeInterval(), False, 'Email and social networking'), Interval(1000, 2, 816, BoundedTimeInterval(), False, 'Add foglib.Session.cases_named method'), Interval(1001, 2, 807, BoundedTimeInterval(), False, 'Implement facebook upload'), Interval(1002, 2, 807, BoundedTimeInterval(), False, 'Implement facebook upload'), Interval(1003, 2, 807, BoundedTimeInterval(), False, 'Implement facebook upload'), Interval(1004, 2, 820, BoundedTimeInterval(), False, 'Email and social networking'), Interval(1005, 2, 826, BoundedTimeInterval(), False, 'Refactor foglib.Interval'), Interval(1006, 2, 826, BoundedTimeInterval(), False, 'Refactor foglib.Interval'), Interval(1007, 2, 825, BoundedTimeInterval(), False, 'Add test cases for fogzap and libraries'), Interval(1008, 2, 821, BoundedTimeInterval(), False, 'Planning'), Interval(1009, 2, 825, OngoingTimeInterval(), False, 'Add test cases for fogzap and libraries')]))

class TestCommand(unittest.TestCase):
    def test_creation_with_function_equal_list_unshared_intervals_function_and_name_equal_list_unshared_intervals_and_short_desc_equal_Lists_the_time_intervals_that_have_not_yet_been_shared_on_social_media(self):
        command = Command('list_unshared_intervals', 'Lists the time intervals that have not yet been shared on social media.', list_unshared_intervals)
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_function_equal_list_unshared_intervals_function_and_name_equal_list_unshared_intervals_and_short_desc_equal_Lists_the_time_intervals_that_have_not_yet_been_shared_on_social_media_case_2(self):
        command = Command('list_unshared_intervals', 'Lists the time intervals that have not yet been shared on social media.', list_unshared_intervals)
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_function_equal_list_unshared_work_times_function_and_name_equal_list_unshared_work_times_and_short_desc_equal_Lists_time_spent_working_for_each_day_that_has_not_been_shared_on_social_media(self):
        command = Command('list_unshared_work_times', 'Lists time spent working for each day that has not been shared on social media.', list_unshared_work_times)
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_function_equal_list_unshared_work_times_function_and_name_equal_list_unshared_work_times_and_short_desc_equal_Lists_time_spent_working_for_each_day_that_has_not_been_shared_on_social_media_case_2(self):
        command = Command('list_unshared_work_times', 'Lists time spent working for each day that has not been shared on social media.', list_unshared_work_times)
        # Make sure it doesn't raise any exceptions.


class TestCommandWithoutLogin(unittest.TestCase):
    def test_creation_with_function_equal_list_commands_function_and_name_equal_list_commands_and_short_desc_equal_Lists_all_commands_accepted_by_fogzap(self):
        command_without_login = CommandWithoutLogin('list_commands', 'Lists all commands accepted by fogzap', list_commands)
        # Make sure it doesn't raise any exceptions.

    def test_creation_with_function_equal_list_commands_function_and_name_equal_list_commands_and_short_desc_equal_Lists_all_commands_accepted_by_fogzap_case_2(self):
        command_without_login = CommandWithoutLogin('list_commands', 'Lists all commands accepted by fogzap', list_commands)
        # Make sure it doesn't raise any exceptions.

class TestListUnsharedIntervals(unittest.TestCase):
    def test_list_unshared_intervals_returns_None_for_args_equal_list_and_last_upload_date_equal_20130221_0000000500_and_session_equal_session_instance(self):
        # obj = <TODO: datetime.datetime>
        # self.assertEqual(None, list_unshared_intervals(Session(), obj, []))
        pass

class TestListUnsharedWorkTimes(unittest.TestCase):
    def test_list_unshared_work_times_returns_None_for_args_equal_list_and_last_upload_date_equal_20130221_0000000500_and_session_equal_session_instance(self):
        # obj = <TODO: datetime.datetime>
        # self.assertEqual(None, list_unshared_work_times(Session(), obj, []))
        pass

class TestShareWorkTimes(unittest.TestCase):
    @unittest.expectedFailure
    def test_share_work_times(self):
        # self.assertEqual(expected, share_work_times(session, last_upload_date, args))

        # TODO: implement your test here
        self.assertTrue(False, "Haven't implemented this test yet")
        

class TestListCommands(unittest.TestCase):
    def test_list_commands_returns_None_for_args_equal_list_and_last_upload_date_equal_20130221_0000000500(self):
        # self.assertEqual(None, list_commands(<TODO: datetime.datetime>, []))
        pass

class TestRunFogzap(unittest.TestCase):
    def test_run_fogzap_returns_None_for_list_case_2(self):
        self.assertEqual(None, run_fogzap(['./fogzap.py', 'list_commands']))



if __name__ == '__main__':
    unittest.main()
