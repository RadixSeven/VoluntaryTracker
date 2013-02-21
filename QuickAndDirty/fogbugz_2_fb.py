#!/usr/bin/python
from __future__ import print_function
import os.path, datetime, sys, pickle
import requests
import xml.etree.ElementTree as ET

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


# Now log off
logoff_resp = requests.get(api_url, params = {'cmd':'logoff','token':token})
print(logoff_resp.text)
