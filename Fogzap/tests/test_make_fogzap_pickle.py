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
from make_fogzap_pickle import run_make_fogzap_pickle

class TestDayMonthYearDate(unittest.TestCase):
    def test_day_month_year_date(self):
        # self.assertEqual(expected, day_month_year_date(date_string))
        assert False # TODO: implement your test here

class TestRunMakeFogzapPickle(unittest.TestCase):
    def test_run_make_fogzap_pickle_raises_1_for_list(self):
        self.assertRaises(int, lambda: run_make_fogzap_pickle(['./make_fogzap_pickle', '--display']))

if __name__ == '__main__':
    unittest.main()
