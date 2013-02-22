#!/usr/bin/python
"""
Library providing access to the fogbugz API

"""
from __future__ import print_function
import os.path, datetime, sys, pickle
import requests
import xml.etree.ElementTree as ET
from tzutil import UTC,LocalTimezone

def fogbugz_datetime(date_str):
    """Return a `datetime.datetime` object with the UTC timezone constructed from the fogbugz date string

    As a special case, returns None when it is passed None

    :param date_str: The date-time string to convert into a `datetime.datetime` object 
    :type date_str: string
    :return: a datetime object with the UTC timezone constructed from the fogbugz date string or None when the input string is None
    :rtype: datetime.datetime or None

    """
    if date_str is None:
        return None
    else:
        dt=datetime.datetime.strptime(date_str,'%Y-%m-%dT%H:%M:%SZ');
        return dt.replace(tzinfo=UTC());

class Interval:
    """Represents an interval recorded by the time-tracking parts of Fogbugz.

    Members:

        interval_id - The id number of this interval

        person_id - The id number of the person working during this
              interval

        case_id - The id number of the case being worked on in this
              interval

        start - A datetime object giving the start of the interval (or
              None because I used the same code as for end)

        end - A datetime object giving the end of the interval (or
              None if the interval is still ongoing)

        deleted Whether this interval was deleted after its creation

        title The title of the case being worked on in this interval
    """
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
        code will die horribly if you violate its
        assumptions. (Actually, the start and the endpoints can be
        missing. If they are, instead of datetime objects, the
        contents of self.start and self.end will be None respectively)
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
                 '(deleted)' if self.deleted else '(not deleted)','>']);

class IncompatibleAPIVersionException:
    """The API is no longer compatible with the version supported by this library

    api_min_ver member contains the minimum allowed api version (a number)

    api_supp_ver member contains the version this library supports (a number)

    """
    def __init__(self, api_min_ver, api_supp_ver):
        """Set the minimum accepted and supported version
        
        api_min_ver - number

        api_supp_ver - number

        """
        self.api_min_ver = api_min_ver
        self.api_supp_ver = api_supp_ver

class IncompatibleAPICallFormatException:
    """The HTML for making API calls has changed and no longer includes a ?

    """
    pass

class LoginException:
    """A session could not log in
    
    xml member holds the xml that indicated the failed response

    TODO: break this into sub-exceptions for the various reasons a login may have failed

    """
    def __init__(self, xml):
        """Create a `LoginException` where the failure response was the string contained in `xml`"""
        self.xml = xml

class Session:
    """A session interacting with fogbugz

    Allows logging on, making queries, and logging off

    _token = string or None. Holds the token used when logged in or None if not logged in
    _address = string or None. Holds the base address for the fogbugz instance or None if not logged in.

    _api_url = string or None. Holds url to use in making calls to requests.get or requests.post or None if not logged in

    """

    def isLoggedIn(self):
        """Return `True` iff this session is currently logged in""" 
        return not( self._token is None )

    def __init__(self):
        """Create a session that is not logged in"""
        self._set_login_dependent_members_to_none()

    def _set_login_dependent_members_to_none(self):
        """Set all the member variables that are None when not logged in to None"""
        self._token = None
        self._address = None
        self._api_url = None

    def login(self, username, password, address):
        """Attempt to log in this session as the given user

        Raises IncompatibleAPIVersionException, IncompatibleAPICallFormatException, or LoginException on error
        """
        self._address = address;

        # Check the API metadata
        api_metadata_resp = requests.get('https://{}/{}'.format(address,'api.xml'))
        api_metadata_root = ET.fromstring(api_metadata_resp.text)

        # Quit if API incompatible
        api_min_ver = float(api_metadata_root.find('minversion').text);
        if api_min_ver > 8:
            self._set_login_dependent_members_to_none()
            raise IncompatibleApiVersionException(api_min_ver, 8)

        # Extract query url fragment and quit if it doesn't end in '?'
        api_url_fragment=api_metadata_root.find('url').text
        last_char = api_url_fragment[-1]
        if last_char == '?':
            api_url_fragment = api_url_fragment[:-1]
        else:
            self._set_login_dependent_members_to_none()
            raise IncompatibleAPICallFormatException()
        
        # Update the address by tacking on the query url without the ?
        self._api_url = ''.join(['https://',address,'/',api_url_fragment])

        # Now log in and get login token
        login_resp = requests.get(self._api_url,
            params = {'cmd':'logon','email':username,'password':password})

        login_root = ET.fromstring(login_resp.text)
        token_elt = login_root.find('token')
        if token_elt is None:
            raise LoginException(login_resp.text)
        else:
            self._token = token_elt.text

    def logoff(self):
        """Ensures that this session has logged off

        If the session is logged on, contacts the server and logs off.
        If not logged on, does nothing.
        """
        if self._token:
            logoff_resp = requests.get(self._api_url, params = {'cmd':'logoff','token':self._token})

    def list_intervals_since(self, start_time):
        """Return the time intervals recorded for the logged in user since the given start time

        start_time - (a time-zone aware datetime object) the earliest
            time a returned interval will start

        """
        
	start_time_UTC = start_time.astimezone(UTC());
        start_time_UTC_str = start_time_UTC.strftime(
            '%Y-%m-%dT%H:%M:%SZ')
        listintervals_resp = requests.get(self._api_url,
            params = {'cmd':'listIntervals','token':self._token,
                      'dtstart':start_time_UTC_str})
        listintervals_root = ET.fromstring(listintervals_resp.text);
        intervals = [Interval(interval) for interval in listintervals_root.find('intervals')]
        return intervals



