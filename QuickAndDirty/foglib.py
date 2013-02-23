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

class CaseAttribute:
    """Represents an optional attribute of a fogbugz case

    In the API documentation, they are alled columns.

    Members: (all are strings)

    name - the name of the attribute

    description - the description of the property represented by the attribute

    sample_data - a string giving sample data content of the html element from the documentation

    """
    def __init__(self, name, sample_data, description):
        """Create a CaseAttribute with the given name, description, and sample_data

        """
        if name and description and sample_data:
            self.name = name
            self.description = description
            self.sample_data
        else:
            raise ValueError("No argument to CaseAttribute's constructor can be None.");

    @staticmethod
    def all():
        """Return all attributes a case can have 

        Note that event is one of the attributes (and events have lots of tags as their payload).
        """
        return [
            ClassAttribute('ixBug','123','case number'),
            ClassAttribute('ixBugParent','234','parent case number'),
            ClassAttribute('ixBugChildren','456,876','subcase numbers'),
            ClassAttribute('tags',""" 
                <tag><![CDATA[first]]></tag>
                <tag><![CDATA[second]]></tag>
                <tag><![CDATA[third]]></tag>""",'tags'),
            ClassAttribute('fOpen','true','true if open, false if closed '),
            ClassAttribute('sTitle','Duck, Duck... but No Goose!','title '),
            ClassAttribute('sOriginalTitle','Problem finding the goose...',
                           'original title for a case opened by an '
                           'incoming email or a public case submission '),
            ClassAttribute('sLatestTextSummary','I searched the docs, '
                           'but no goose!','short string with case\'s '
                           'latest comment '),
            ClassAttribute('ixBugEventLatestText','1151','ixBugEvent '
                           'for latest event with actual text comment '),
            ClassAttribute('ixProject','22','project id '),
            ClassAttribute('sProject','The Farm','project name '),
            ClassAttribute('ixArea','35','area id '),
            ClassAttribute('sArea','Pond','area name '),
            ClassAttribute('ixGroup','6','group id (deprecated as of '
                           'FogBugz 8--will always return 0) '),
            ClassAttribute('ixPersonAssignedTo','1','person case is '
                           'assigned to (id) '),
            ClassAttribute('sPersonAssignedTo','Old MacDonald','person case '
                           'is assigned to (name) '),
            ClassAttribute('sEmailAssignedTo','grandpa@oldmacdonald.com',
                           'email of person case is assigned to '),
            ClassAttribute('ixPersonOpenedBy','2','person case was '
                           'opened by (id) '),
            ClassAttribute('ixPersonResolvedBy','2','person case was '
                           'resolved by (id) '),
            ClassAttribute('ixPersonClosedBy','','person case was closed '
                           'by (id) '),
            ClassAttribute('ixPersonLastEditedBy','0','person case was '
                           'last edited by (id) '),
            ClassAttribute('ixStatus','2','status (id) '),
            ClassAttribute('ixBugDuplicates','321','cases that are closed '
                           'as duplicates of this one (id) '),
            ClassAttribute('ixBugOriginal','654','the case which this '
                           'one was a duplicate of (id) '),
            ClassAttribute('sStatus','Geschlossen (Fixed)','status (name) '),
            ClassAttribute('ixPriority','3','priority (id) '),
            ClassAttribute('sPriority','Must Fix','priority (name) '),
            ClassAttribute('ixFixFor','3','fixfor (id) '),
            ClassAttribute('sFixFor','Test','fixfor (name) '),
            ClassAttribute('dtFixFor','2007-05-06T22:47:59Z','date of '
                           'fixfor (date) '),
            ClassAttribute('sVersion','','version field (custom field #1) '),
            ClassAttribute('sComputer','','computer field (custom field #2) '),
            ClassAttribute('hrsOrigEst','0',
                           'hours of original estimate (0 if no estimate) '),
            ClassAttribute('hrsCurrEst','0','hours of current estimate '),
            ClassAttribute('hrsElapsed','0',
                           'includes all time from time intervals PLUS '
                           'hrsElapsedExtra time '),
            ClassAttribute('c','0','number of occurrences (minus 1) of this '
                           'bug (increased via bugzscout -- to display the '
                           'actual number of occurrences, add 1 to this '
                           'number '),
            ClassAttribute('sCustomerEmail','','if there is a customer '
                           'contact for this case, this is their email '),
            ClassAttribute('ixMailbox','0','if this case came in via '
                           'dispatcho, the mailbox it came in on '),
            ClassAttribute('ixCategory','1','category (id) '),
            ClassAttribute('sCategory','Feature','category (name) '),
            ClassAttribute('dtOpened','2007-05-06T22:47:59Z',
                           'date case was opened '),
            ClassAttribute('dtResolved','2007-05-06T22:47:59Z',
                           'date case was resolved '),
            ClassAttribute('dtClosed','2007-05-06T22:47:59Z',
                           'date case was closed '),
            ClassAttribute('ixBugEventLatest','1151','latest bugevent '),
            ClassAttribute('dtLastUpdated','2007-05-06T22:47:59Z',
                           'the date when this case was last updated'),
            ClassAttribute('fReplied','false',
                           'has this case been replied to? '),
            ClassAttribute('fForwarded','false',
                           'has this case been forwarded? '),
            ClassAttribute('sTicket','','id for customer to view bug '
                           '(bug number + 8 letters e.g. 4003_XFLFFFCS) '),
            ClassAttribute('ixDiscussTopic','0','id of discussion topic if '
                           'case is related '),
            ClassAttribute('dtDue','','date this case is due (empty if no '
                           'due date) '),
            ClassAttribute('sReleaseNotes','','release notes '),
            ClassAttribute('ixBugEventLastView','1151','the ixBugEventLatest '
                           'when you last viewed this case '),
            ClassAttribute('dtLastView','2007-05-06T22:47:59Z','the date '
                           'when you last viewed this case '),
            ClassAttribute('ixRelatedBugs','345,267,2920','comma separated '
                           'list of other related case numbers '),
            ClassAttribute('sScoutDescription','Main.cpp:165','if this case '
                           'is a Scout case, this ID is the unique '
                           'identifier '),
            ClassAttribute('sScoutMessage','Please contact us or visit our '
                           'knowledge base to resolve.','this is the '
                           'message -- displayed to users when they submit a '
                           'case that matches this sScoutDescription '),
            ClassAttribute('fScoutStopReporting','false','whether we are '
                           'still recording occurrences of this crash or not'),
            ClassAttribute('fSubscribed','true','true if you are subscribed '
                           'to this case, otherwise false'),
            ClassAttribute('events',
                           """<event ixBugEvent="174" ixBug="13">\n"""

                           """<ixBugEvent>174</ixBugEvent> -- Identity """
                           """field in the database for this event\n"""

                           """<evt>4</evt> -- Number for type of event, """
                           """see event codes\n"""

                           """<sVerb>Assigned to Captain Caveman</sVerb> """
                           """-- Description of event in English always\n"""

                           """<ixPerson>3</ixPerson> -- Identity field of """
                           """the person who made this event happen\n"""

                           """<sPerson>Mikey</sPerson> -- Person's full """
                           """name\n"""

                           """<ixPersonAssignedTo>4</ixPersonAssignedTo> """
                           """-- Identity field of the person this case """
                           """is assigned to\n"""

                           """<dt>2007-05-06T22:47:59Z</dt> -- Date """
                           """event happened (in RFC822 UTC format)\n"""

                           """<s>Up up and away!</s> -- The text of the """
                           """event (if this is an email or was created in """
                           """HTML mode via Rich Case Events, this is a """
                           """plain-text version of the event)\n"""

                           """<sHTML><![CDATA[<strong>Up up and """
                           """away!</strong>]]></sHTML> -- If this is """
                           """an event created in HTML mode via Rich """
                           """Case Events, this contains the raw HTML """
                           """version of the event\n"""

                           """<fEmail>false</fEmail> -- True if it is """
                           """an email event\n"""

                           """<bEmail>false</bEmail> -- Deprecated: use """
                           """fEmail\n"""

                           """<fExternal>false</fExternal> -- True if """
                           """this case was created via an incoming """
                           """email, discussion topic, or BugzScout\n"""

                           """<bExternal>false</bExternal> -- Deprecated: """
                           """use fExternal\n"""

                           """<fHTML>true</fHTML> -- True if the event is """
                           """an email and the html version has been """
                           """cached. You should not need to look at """
                           """this field. Instead use fEmail to determine """
                           """if the event is an email and sFormat """
                           """to determine if an edit is html-formatted\n"""

                           """<sFormat>html</sFormat> -- 'html' if """
                           """the event was created in HTML mode via """
                           """Rich Case Events\n"""
                           
                           """<sChanges>Project changed from 'Inbox' to """
                           """'Cave'.</sChanges> -- Description of """
                           """changes to the case during this event\n"""

                           """<evtDescription>Captain Caveman von Mikey """
                           """zugewiesen</evtDescription> -- Description """
                           """of event in YOUR language (in this """
                           """case German)\n"""

                           """\n"""
                           """<rgAttachments>\n"""
                           """    <attachment>\n"""

                           """        <sFileName>Test Word.doc"""
                           """</sFileName> -- name of the attached file\n"""

                           """        <sURL>default.asp?pg=pgDownload"""
                           """&amp;pgType=pgAttachment&amp;ixBugEvent"""
                           """=756&amp;sPart=2&amp;sTicket=&amp;"""
                           """sFileName=Test%20Word.doc</sURL> -- url """
                           """to hit to get the contents of the"""
                           """ attached file (add on token=<yourtoken>)\n"""

                           """    </attachment>\n"""
                           """</rgAttachments>\n"""
                           """\n"""

                           """-- if the event is an email """
                           """(fEmail == true) then there are """
                           """additional fields --\n"""

                           """\n"""

                           """<sFrom>"JJ Walker" <jj@dynomite.org></sFrom> """
                           """-- the from header from the message\n"""

                           """<sTo>good@times.org</sTo> -- the to header """
                           """from the message\n"""

                           """<sCC></sCC> -- the cc header from the """
                           """message\n"""

                           """<sBCC></sBCC> -- the bcc header from the """
                           """message (if readable)\n"""

                           """<sReplyTo></sReplyTo> -- the replyto header """
                           """from the message\n"""

                           """<sSubject></sSubject> -- the subject header """
                           """from the message\n"""

                           """<sDate>5 Jun 07 21:07:54 GMT</sDate> -- the """
                           """date header from the message (exactly as """
                           """it appears usually rfc822 date)\n"""

                           """<sBodyText></sBodyText> -- the body plaintext """
                           """from the message\n"""

                           """<sBodyHTML></sBodyHTML> -- the message """
                           """formatted in html\n"""

                           """\n"""

                           """</event>\n"""
                           ,'Include to receive the list of all events '
                           'for the class')
            ];

    @classmethod
    def from_name(cls, name):
        """Return the ClassAttribute corresponding to the given name

        Raises ValueError if there is no class attribute with that name
        """
        return cls.all().index(name)


class UnparsedCaseValue:
    """Represents the value of a case attribute that has not been parsed

    Attributes:

    attribute - the CaseAttribute object of which this is a value

    text - the string for the given attribute (includes the xml for
        the elment itself)

    """
    def __init__(self, attribute, text):
        """Create an UnparsedCaseValue with the given attribute and text attributes"""
        self.attribute = attribute
        self.text = text

class Case:
    """A case in fogbugz

    Attributes:

    id - integer - the id of this case (If not present, 0 or None)

    parent - integer - the id of the parent of this case (If not
        present, 0 or None)

    title - string - the title of this case (None if not present)

    hoursElapsed - float - total elapsed hours -- includes all time
        from time intervals PLUS hrsElapsedExtra time. 0 if not present

    unparsed - array of UnparsedCaseValue objects for all the
        attributes returned for this case. 

        This list includes id, parent and others that have also been
        made into class attributes (incidentally, the class attributes
        are called different names from the xml tags).  Retaining the
        unparsed versions keeps backwards compatibility. As more and
        more attributes are parsed, any code using the unparsed
        version will still work.

    """

    def __init__(self, root):
        """Create a case whose attributes are the children of root

        root is an xml.etree.ElementTree.Element representing
        Fogbugz's xml encoding for a case.

        raises ValueException if one of the children of root is not a
        known case name
        
        """
        self.id = None
        self.parent = None
        self.title = None
        self.hoursElapsed = 0
        self.unparsed = []
        for child in root:
            name = child.tag
            attr = CaseAttribute.from_name(name)
            self.unparsed.extend(UnparsedCaseValue(attr, child.tostring()))
            if   'ixBug' == name:
                self.id = int(child.text)
            elif 'ixBugParent' == name:
                self.parent = int(child.text)
            elif 'sTitle' == name:
                self.title = child.text
            elif 'hrsElapsed' == name:
                self.hoursElapsed = float(child.text)
        
                
    
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


