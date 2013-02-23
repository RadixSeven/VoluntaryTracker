#!/usr/bin/python
from __future__ import print_function
import os.path, datetime, sys, pickle
import requests
import xml.etree.ElementTree as ET
from tzutil import UTC,LocalTimezone
import config_file
import foglib

# Read the configuration variables
success = False
try:
    with open(config_file.fogbugz_loc, 'rb') as f:
        username, password, address = pickle.load(f)
    with open(config_file.last_upload_date_loc, 'rb') as f:
        last_upload_date = pickle.load(f)
except:
    print('Could not read configuration files. Use the make_fogzap_pickle to create the configuration files.');
    sys.exit(0)

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


intervals = session.list_intervals_since(last_upload_date)

for i in intervals:
    print(i)

session.logoff();
