#!/usr/bin/python
from __future__ import print_function
import os.path, datetime, sys, pickle
import requests
import xml.etree.ElementTree as ET
from tzutil import UTC,LocalTimezone

def fogbugz_datetime(date_str):
    """Returns a datetime object with the UTC timezone constructed from the fogbugz date string

    As a special case, returns None when it is passed None
    """
    if date_str is None:
        return None
    else:
        dt=datetime.datetime.strptime(date_str,'%Y-%m-%dT%H:%M:%SZ');
        return dt.replace(tzinfo=UTC());

class FogbugzInterval:
    def __init__(self, interval_element):
        """Takes an xml interval element (xml.etree.ElementTree.Element) and constructs an Interval object containing all its data

        It is assumed that the the interval element is the root of a
        tree with the following children (I've left the content in for
        use as an example):
        
        <ixInterval>944</ixInterval>
        <ixPerson>2</ixPerson>
        <ixBug>767</ixBug>
        <dtStart>2013-02-19T00:26:00Z</dtStart>
        <dtEnd>2013-02-19T00:41:00Z</dtEnd>
        <fDeleted>false</fDeleted>
        <sTitle>Computer maintenance</sTitle>

        It is assumed that there is exactly one of each child and the
        code will die horribly if you violate its assumptions.
        """
        # Extract from xml tree
        self.interval_id = int(interval_element.find('ixInterval').text)
        self.person_id = int(interval_element.find('ixPerson').text)
        self.case_id = int(interval_element.find('ixBug').text)
        self.start = fogbugz_datetime(interval_element.find('dtStart').text)
        self.end = fogbugz_datetime(interval_element.find('dtEnd').text)
        self.deleted = interval_element.find('fDeleted').text == 'true'
        self.title = interval_element.find('sTitle').text

        # Adjust start and endpoints to local time zone if they are not None
        local = LocalTimezone();
        if self.start:
            self.start = self.start.astimezone(local);
        if self.end:
            self.end = self.end.astimezone(local);

    def __str__(self):
        return repr(self)
    def __repr__(self):
        return ''.join(['<',
                 'ID:',      str(self.interval_id),' ',
                 'Person:',  str(self.person_id),' ',
                 'Case:',    str(self.case_id),' ',
                 str(self.start),' - ',str(self.end), ' ',
                 '(deleted)' if self.deleted else '(present)','>']);

# Set up directory location constants
#
# TODO: move these to their own module or whatever the convention is
# for shared constants in Python
pickle_dir = os.path.join(os.path.expanduser('~'),'.config','fogbugz_2_fb')
fogbugz_loc = os.path.join(pickle_dir,'fogbugz.pickle')
last_upload_date_loc = os.path.join(pickle_dir,'last_upload.pickle')

# Read the configuration variables
success = False
try:
    with open(fogbugz_loc, 'rb') as f:
        username, password, address = pickle.load(f)
    with open(last_upload_date_loc, 'rb') as f:
        last_upload_date = pickle.load(f)
except:
    print('Could not read configuration files. Use the make_fogbugz_2_fb_pickle to create the configuration files.');
    sys.exit(0)

# Check the API metadata
api_metadata_resp = requests.get('https://{}/{}'.format(address,'api.xml'))
api_metadata_root = ET.fromstring(api_metadata_resp.text)

# Quit if API incompatible
api_min_ver = float(api_metadata_root.find('minversion').text);
if api_min_ver > 8:
    print('Fogbugz api has changed incompatibly since version 8 where this code was written. Minimum version is now {}. Quitting.'.format(api_min_ver),
          file = sys.stderr)
    sys.exit(0)

# Extract query url fragment and quit if it doesn't end in '?'
api_url_fragment=api_metadata_root.find('url').text
last_char = api_url_fragment[-1]
if last_char == '?':
    api_url_fragment = api_url_fragment[:-1]
else:
    print('Method of making api calls has changed - query url fragment no longer ends in a ?. Cannot continue until someone has updated the program for the new calling parameter.', file = sys.stderr)
    sys.exit(0)

# Update the address by tacking on the query url without the ?
api_url = ''.join(['https://',address,'/',api_url_fragment])

# Now log in and get login token
login_resp = requests.get(api_url,
    params = {'cmd':'logon','email':username,'password':password})

login_root = ET.fromstring(login_resp.text)
token_elt = login_root.find('token')
if token_elt is None:
    print('Could not log on to fogbugz. Actual xml returned is {}'.
          format(login_resp.text), file = sys.stderr)
    sys.exit(0)

token = token_elt.text

# Now list the work intervals since the last successful upload
last_upload_date_UTC = last_upload_date.astimezone(UTC());
last_upload_date_UTC_str = last_upload_date_UTC.strftime(
    '%Y-%m-%dT%H:%M:%SZ')
listintervals_resp = requests.get(api_url,
    params = {'cmd':'listIntervals','token':token,
              'dtstart':last_upload_date_UTC_str})
listintervals_root = ET.fromstring(listintervals_resp.text);
intervals = [FogbugzInterval(interval) for interval in listintervals_root.find('intervals')]

for i in intervals:
    print(str(i))

# Now log off
logoff_resp = requests.get(api_url, params = {'cmd':'logoff','token':token})

