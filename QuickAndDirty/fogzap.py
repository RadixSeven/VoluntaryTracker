#!/usr/bin/python
from __future__ import print_function
import os.path, datetime, sys, pickle, argparse, textwrap, inspect
import xml.etree.ElementTree as ET

import requests

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
            print(('Fogbugz api has changed incompatibly since version {} '
                  'where this code was written. Minimum version is now {}. '
                   'Quitting.').format(e.api_supp_ver, e.api_min_ver),
                  file = sys.stderr)
            sys.exit(0)
        except IncompatibleAPICallFormatException:
            print('Method of making api calls has changed - query url fragment '
                  'no longer ends in a ?. Cannot continue until someone has '
                  'updated the program for the new calling parameter.', 
                  file = sys.stderr)
            sys.exit(0)
        except LoginException as e:
            print(('Could not log on to fogbugz. '
                  'Actual xml returned is {}').format(login_resp.text), 
                  file = sys.stderr)
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
    
    days = {}
    for i in intervals:
        start = i.start if i.start else last_upload_date
        start_day = start.date()
        end = i.end if i.end else datetime.datetime.now(LocalTimezone())
        end_day = end.date()
            
        if start_day != end_day:
            print('Warning: interval {} starts and ends on different days. '
                  'Counting it in the start day only', file=sys.stderr)
        duration = (end - start).total_seconds()
        if not i.deleted:
            if not days.has_key(start_day):
                days[start_day] = 0
            days[start_day] += duration

    for day in sorted(days.keys()):
        print('{}: {} hours'.format(str(day), days[day]/3600))
        
    


all_commands[
    'list_unshared_work_times'] = Command('list_unshared_work_times',
                                         'Lists time spent working for '
                                         'each day that has not been '
                                         'shared on social media.', 
                                         list_unshared_work_times)


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


username, password, address, last_upload_date = read_configuration_variables()


#################
#
# Main code
#
#################

# Handle command line arguments
parser = argparse.ArgumentParser(description='Miscelaneous utilities for '
                                 'interacting with fogbugz');
parser.add_argument('command', help='The command to execute. All commands '
                    'take a -h option to print details of what arguments '
                    'they take. The list_commands command will list all '
                    'the commands with a short description.');
parser.add_argument('arguments', nargs=argparse.REMAINDER, 
                    help='All arguments to the command');
args = parser.parse_args()



# Execute the selected command or print help if the command does not exist
if all_commands.has_key(args.command.lower()):
    all_commands[args.command.lower()].execute(
        username, password, address, last_upload_date, args.arguments)
else:
    parser.print_help()




