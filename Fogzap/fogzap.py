#!/usr/bin/python

# Standard libraries
import os.path, datetime, sys, pickle, argparse, textwrap, inspect
import xml.etree.ElementTree as ET

# 3rd Party packages
import requests
import fbconsole

# Local modules
from tzutil import UTC,LocalTimezone
import config_file
import foglib

#################
#
# Utility functions
#
#################


def read_configuration_variables():
    """Read the configuration variables"""
    success = False
    try:
        with open(config_file.fogbugz_loc, 'rb') as f:
            username, password, address = pickle.load(f)
        with open(config_file.last_upload_date_loc, 'rb') as f:
            last_upload_date = pickle.load(f)
        return (username, password, address, last_upload_date)
    except:
        print('Could not read configuration files. '
              'Use the make_fogzap_pickle to create the configuration files.');
        sys.exit(0)

def time_interval_for_day_containing( a_datetime, a_timezone ):
    """Returns a BoundedTimeInterval for the 24 hour day containing a_datetime in a_timezone

    A day has its first microsecond at 0:0:0 and its last microsecond
    is the microsecond before 0:0:0 the next day.

    a_datetime - a timezone aware datetime object

    a_timezone - the timezone where the day is measured

    """
    instant_in_correct_tz = a_datetime.astimezone(a_timezone)
    first = instant_in_correct_tz.replace(
        hour=0, minute=0, second=0, microsecond=0);
    last = (first + datetime.timedelta(days=1) - 
            datetime.timedelta(microseconds=1))
    return foglib.BoundedTimeInterval(first, last)

def split_into_days( a_TimeInterval ):
    """Split a_TimeInterval so that the parts each lie in only one day.

    Returns a list of non-overlapping BoundedTimeInterval objects
    whose union is a_TimeInterval and whose start and end points lie
    in the same day. OngoingTimeInterval objects are treated as if
    they ended at LocalTimezone.now(). EmptyTimeInterval objects cause
    an empty list to be returned.

    """

    # Deal with ongoing intervals by bounding them at the present
    if a_TimeInterval.is_ongoing():
       remaining = foglib.BoundedTimeInterval(
           a_TimeInterval.first, LocalTimezone.now())
    else:
        remaining = a_TimeInterval

    localtz = LocalTimezone()
    result = []
    try:
        while(True):
            # Slice off the last day or part of a day in the interval
            # and add it to the result
            last_day = time_interval_for_day_containing( 
                remaining.last, localtz )
            overlap = remaining.intersection_with(last_day)
            #sys.stderr.write('Overlap: {}\n'.format(repr(overlap)))
            result.append(overlap)
            # Update remaining to include everything before the first
            # instant of the last day.
            remaining = remaining.subinterval_before(last_day.first)
    except AttributeError as e:
        pass # Stop when remaining is an empty interval and thus has no
             # last attribute.

    return result
    
def summarize_intervals_by_day(intervals):
    """Return the number of hours covered by the given intervals in each day

    intervals - an iterable sequence of non-overlapping
        foglib.Interval objects. Each day in the output contains the
        sum of the durations of the intervals for that date. Ongoing
        intervals are treates as if they ended now.

    return - a dictionary in which each key is a date and each value
        is a float giving the number of hours worked on that date (as
        determined by the local timezone.
    """
    # Make a list of intervals split so they don't overlap a day boundary
    extant = [i for i in intervals if not i.deleted]
    split_intervals_l = [split_into_days(i.time_interval) for i in extant]
    split_intervals = [i for sublist in split_intervals_l for i in sublist]
    
    # For each interval, add its duration to the day in which it falls
    days = {}
    for i in split_intervals:
        start_day = i.first.date()
        end_day = i.last.date()
            
        assert( start_day == end_day) # Make sure the splitting workede

        duration = i.duration().total_seconds()
        if days.has_key(start_day):
            days[start_day] += duration
        else:
            days[start_day] = duration
    return days

#################
#
# Set up commands
#
#################

# TODO: come up with a way to not pass last_upload_date to everything
# it will only be needed by a small subset of commands. In general,
# commands may require state saved between sessions. Maybe just pass a
# dictionary of remembered state and configuration data? Right now
# it's just one variable, so it's livable. I won't worry about it
# unless I have lots of extra time or I need to add another variable.

class Command(object):
    """Represents a subcommand that fogzap can execute

    Members:

    name - name of the command used on the command line to invoke 
        it. cannot contain spaces

    short_desc - the description printed by the list_commands function

    function - the function to call to execute the command. It must
        take three arguments, the first of which is a fogbugz
        session. The second is the date of the last upload to Facebook
        (an aware datetime object) The final argument is a list of
        strings containing the arguments passed on the command line to
        the subcommand

        callable using: self.function(session, last_upload_date, args)


    """
    def __init__(self, name, short_desc, function):
        self.name = name
        self.short_desc = short_desc
        assert callable(function)
        assert 3==len(inspect.getargspec(function).args)
        self.function = function

    def execute(self, username, password, address, last_upload_date, args):
        """Execute the command with its arguments

        username, password, address - strings used to log in 
            and create the session

        last_upload_date - a timezone aware datetime containing the last time 
            the data was uploaded to facebook
        
        args - a list of strings - the arguments passed to the subcommand

        """

        # Log in
        session = foglib.Session();
        try:
            session.login(username, password, address)
        except IncompatibleAPIVersionException as e:
            sys.stderr.write(('Fogbugz api has changed incompatibly since '
                              'version {} where this code was written. '
                              'Minimum version is now {}. Quitting.').
                             format(e.api_supp_ver, e.api_min_ver))
            sys.exit(0)
        except IncompatibleAPICallFormatException:
            sys.stderr.write(
                'Method of making api calls has changed - ''query url fragment '
                'no longer ends in a ?. Cannot continue until someone has '
                'updated the program for the new calling parameter.')
            sys.exit(0)
        except LoginException as e:
            sys.stderr.write(
                ('Could not log on to fogbugz. '
                 'Actual xml returned is {}').format(login_resp.text))
            sys.exit(0)
        
        # Execute the function
        self.function(session, last_upload_date, args)

        # Log out
        session.logoff();


class CommandWithoutLogin(Command):
    """Represents a subcommand that fogzap can execute without logging into fogbugz

    Members:

    name - name of the command used on the command line to invoke 
        it. cannot contain spaces

    short_desc - the description printed by the list_commands function

    function - the function to call to execute the command. It must
        take two arguments: last successful upload date (an aware
        datetime) and a list of strings containing the arguments
        passed on the command line to the subcommand

        callable using: self.function(last_upload_date, args)

    """
    def __init__(self, name, short_desc, function):
        self.name = name
        self.short_desc = short_desc
        assert callable(function)
        assert 2==len(inspect.getargspec(function).args)
        self.function = function

    def execute(self, username, password, address, last_upload_date, args):
        """Execute the command with its arguments
        username, password, address - ignored
        
        args - a list of strings - the arguments passed to the subcommand

        """

        # Execute the function
        self.function(last_upload_date, args)


all_commands = {}; # Each entry in all commands is a key (the command
                   # name string) and a value (the command
                   # object). The key and name should be lower-case

def list_unshared_intervals(session, last_upload_date, args):
    """Executes the list_unshared_intervals command

    session - a login session

    last_upload_date - a timezone aware datetime - the date of the
        last successful upload to facebook

    args - a list of strings - the arguments passed to the subcommand

    """
    parser = argparse.ArgumentParser(prog = 'list_unshared_intervals')
    a = parser.parse_args(args=args)

    intervals = session.list_intervals_since(last_upload_date)
    
    for i in intervals:
        print(i)

all_commands[
    'list_unshared_intervals'] = Command('list_unshared_intervals',
                                         'Lists the time intervals that '
                                         'have not yet been shared on '
                                         'social media.', 
                                         list_unshared_intervals)


def list_unshared_work_times(session, last_upload_date, args):
    """Executes the list_unshared_work_times command

    session - a login session

    last_upload_date - a timezone aware datetime - the date of the
        last successful upload to facebook

    args - a list of strings - the arguments passed to the subcommand

    """
    parser = argparse.ArgumentParser(prog = 'list_unshared_work_times')
    a = parser.parse_args(args=args)

    intervals = session.list_intervals_since(last_upload_date)

    days = summarize_intervals_by_day(intervals)
    
    for day in sorted(days.keys()):
        print('{}: {} hours'.format(str(day), days[day]/3600))


all_commands[
    'list_unshared_work_times'] = Command('list_unshared_work_times',
                                         'Lists time spent working for '
                                         'each day that has not been '
                                         'shared on social media.', 
                                         list_unshared_work_times)


def share_work_times(session, last_upload_date, args):
    """Executes the share_work_times command

    session - a login session

    last_upload_date - a timezone aware datetime - the date of the
        last successful upload to facebook

    args - a list of strings - the arguments passed to the subcommand

    """
    parser = argparse.ArgumentParser(prog = 'list_unshared_work_times')
    a = parser.parse_args(args=args)

    intervals = session.list_intervals_since(last_upload_date)
    
    days = summarize_intervals_by_day(intervals)
    
    fbconsole.AUTH_SCOPE = ['publish_stream']
    fbconsole.authenticate()

    today = LocalTimezone.now().date()

    for day in sorted(days.keys()):
        if day < today:
            msg = 'I worked {} hours on {}'.format(days[day]/3600, str(day))
            fbconsole.post( '/me/feed/',{'message':msg} )

all_commands[
    'share_work_times'] = Command('share_work_times',
                                  'For each unshared day, shares the time '
                                  'spent working that day on Facebook and '
                                  'marks that day as shared. Does not '
                                  'share the stats for today.', 
                                  share_work_times)


def list_commands(last_upload_date, args):
    """Executes the list_commands subcommand
    args - a list of strings - the arguments passed to the subcommand

    """
    parser = argparse.ArgumentParser(prog='list_commands');
    a = parser.parse_args(args=args)

    hanging_indent=textwrap.TextWrapper(subsequent_indent='    ');
    for c in all_commands.values():
        print(hanging_indent.fill('{} -- {}'.format(c.name, c.short_desc)))

all_commands[
    'list_commands'] = CommandWithoutLogin('list_commands',
                               'Lists all commands accepted by fogzap', 
                               list_commands)



#################
#
# Main code
#
#################

def run_fogzap(cmd_args):
    username, password, address, last_upload_date = read_configuration_variables()
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Miscelaneous utilities for '
                                     'interacting with fogbugz');
    parser.add_argument('command', help='The command to execute. All commands '
                        'take a -h option to print details of what arguments '
                        'they take. The list_commands command will list all '
                        'the commands with a short description.');
    parser.add_argument('arguments', nargs=argparse.REMAINDER, 
                        help='All arguments to the command');
    args = parser.parse_args(args = cmd_args[1:])



    # Execute the selected command or print help if the command does not exist
    if all_commands.has_key(args.command.lower()):
        all_commands[args.command.lower()].execute(
            username, password, address, last_upload_date, args.arguments)
    else:
        parser.print_help()


if __name__ == '__main__':
    run_fogzap(sys.argv)
