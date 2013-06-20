#!/usr/bin/python
#from __future__ import print_function
import argparse, os.path, datetime, sys, pickle, errno
import config_file
from tzutil import LocalTimezone
import tzutil

# Utility function used by the command line arguments to parse a date
def day_month_year_date(date_string):
    try:
        d = datetime.datetime.strptime(date_string, '%d %b %Y')
        d = d.replace(tzinfo=LocalTimezone())
        return d
    except:
        msg = "The date must be in the format: 25 Dec 1955 (you might need quotes around the date to make it a single argument)"
        raise argparse.ArgumentTypeError(msg)

def run_make_fogzap_pickle(cmd_args):

    # Make the configuration directory if it does not exist
    try:
        os.makedirs(config_file.pickle_dir)
    except OSError as exc: 
        if exc.errno == errno.EEXIST and os.path.isdir(config_file.pickle_dir):
            pass #Ignore when directory already exists
        else: 
            stderr.write('Could not ensure that "{}" was a directory'.format(
                    config_file.pickle_dir))
            sys.exit(0)

    # Read in old vlaues for the configuration variables
    success = False
    if os.path.isfile(config_file.fogbugz_loc):
        with open(config_file.fogbugz_loc, 'rb') as f:
            try:
                username, password, address = pickle.load(f)
                success = True
            except: pass
    if not success:
        username = None
        password = None
        address = None

    success = False
    if os.path.isfile(config_file.last_upload_date_loc):
        with open(config_file.last_upload_date_loc, 'rb') as f:
            try: 
                last_upload_date = pickle.load(f)
                success = True
            except: pass

    if not success:
        last_upload_date = None

    # Read the command line arguments
    parser = argparse.ArgumentParser(description='Write values to pickle files '
                                     'used to configure fogzap. Any omitted '
                                     'values will not be written.')
    parser.add_argument('-a', dest = 'address', action = 'store',
                        help = 'The fogbugz address. Example: '
                        'ericmoyer.fogbugz.com')
    parser.add_argument('-u', dest = 'username', action = 'store', 
                        help = "The fogbugz username.")
    parser.add_argument('-p', dest = 'password', action = 'store', 
                        help = "The fogbugz password.")   
    parser.add_argument('-d', dest = 'last_upload_date', action = 'store', 
                        type = day_month_year_date,
                        help = "The last day for which a time measurement was "
                        "successfully uploaded.  Example: 19 Feb 2005")

    parser.add_argument('--display', dest = 'display', action = 'store_const', 
                        const = True, default = False,
                        help = "Just display the current values without "
                        "changing them")   

    args = parser.parse_args(cmd_args[1:])
    if not (args.address or args.username or args.password or 
            args.last_upload_date or args.display):
        parser.print_help()
        sys.exit(0)

    # Handle the display command

    if args.display:
        print 'Username:', str(username)
        print 'Password:', str(password)
        print 'Address:', str(address)
        if last_upload_date is None:
            last_upload_date_str = 'None'
        else:
            if tzutil.is_naive(last_upload_date):
                last_upload_date_str = '{} (no timezone information)'.format(
                    str(last_upload_date))
            else:
                last_upload_date_str = '{} (includes timezone information)'.format(
                    str(last_upload_date))
        print 'Last upload date:', last_upload_date_str
        sys.exit(-1)

    # Set (and possibly write) any new values for fogbugz.pickle

    write_fogbugz_loc = False

    if not (args.username is None):
        username = args.username
        write_fogbugz_loc = True

    if not (args.password is None):
        password = args.password
        write_fogbugz_loc = True

    if not (args.address is None):
        address = args.address
        write_fogbugz_loc = True

    if write_fogbugz_loc:
        try:
            with open(config_file.fogbugz_loc, 'wb') as f:
                pickle.dump([username, password, address], f)
        except IOError as e:
            stderr.write('Error writing to %r\n' % config_file.fogbugz_loc)
            sys.exit(0)

    # Set (and possibly write) any new values for last_upload.pickle

    write_last_upload_date_loc = False

    if not (args.last_upload_date is None):
        last_upload_date = args.last_upload_date
        write_last_upload_date_loc = True

    if write_last_upload_date_loc:
        try:
            with open(config_file.last_upload_date_loc, 'wb') as f:
                pickle.dump(last_upload_date, f)
        except IOError as e:
            stderr.write('Error writing to %r\n' % 
                         config_file.last_upload_date_loc)
    
            sys.exit(0)

if __name__ == '__main__':
    run_make_fogzap_pickle(sys.argv)
