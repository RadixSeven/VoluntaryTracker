#!/usr/bin/python3
import argparse, os.path, datetime, sys, pickle

# Utility function used by the command line arguments to parse a date
def day_month_year_date(date_string):
    try:
        d = datetime.datetime.strptime(date_string, '%d %b %Y')
        return d
    except:
        msg = "The date must be in the format: 25 Dec 1955"
        raise argparse.ArgumentTypeError(msg)

# Set up directory location constants
#
# TODO: move these to their own module or whatever the convention is
# for shared constants in Python
pickle_dir = os.path.join(os.path.expanduser('~'),'.config','fogbugz_2_fb')
fogbugz_loc = os.path.join(pickle_dir,'fogbugz.pickle')
last_upload_date_loc = os.path.join(pickle_dir,'last_upload.pickle')

# Make the configuration directory if it does not exist
os.makedirs(pickle_dir, exist_ok=True)

# Read in old vlaues for the configuration variables
success = False
if os.path.isfile(fogbugz_loc):
    with open(fogbugz_loc, 'rb') as f:
        try:
            username, password, address = pickle.load(f)
            success = True
        except: pass
if not success:
    username = None
    password = None
    address = None

success = False
if os.path.isfile(last_upload_date_loc):
    with open(last_upload_date_loc, 'rb') as f:
        try: 
            last_upload_date = pickle.load(f)
            success = True
        except: pass

if not success:
    last_upload_date = None

# Read the command line arguments
parser = argparse.ArgumentParser(description='Write values to pickle files used to configure fogbugz_2_fb. Any omitted values will not be written.')
parser.add_argument('-a', dest = 'address', action = 'store',
                    help = 'The fogbugz address. Example: ericmoyer.fogbugz.com')
parser.add_argument('-u', dest = 'username', action = 'store', 
                    help = "The fogbugz username.")
parser.add_argument('-p', dest = 'password', action = 'store', 
                    help = "The fogbugz password.")   
parser.add_argument('-d', dest = 'last_upload_date', action = 'store', 
                    type = day_month_year_date,
                    help = "The last day for which a time measurement was successfully uploaded.  Example: 19 Feb 2005")

parser.add_argument('--display', dest = 'display', action = 'store_const', 
                    const = True, default = False,
                    help = "Just display the current values without changing them")   

args = parser.parse_args()
if not (args.address or args.username or args.password or args.last_upload_date or args.display):
    parser.print_help()
    sys.exit(0)

# Handle the display command

if args.display:
    print('Username:', str(username))
    print('Password:', str(password))
    print('Address:', str(address))
    print('Last upload date:', str(last_upload_date),'\n')
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
        with open(fogbugz_loc, 'wb') as f:
            pickle.dump([username, password, address], f)
    except IOError as e:
        print('Error writing to %r' % fogbugz_loc, file=sys.stderr)
        sys.exit(0)

# Set (and possibly write) any new values for last_upload.pickle

write_last_upload_date_loc = False

if not (args.last_upload_date is None):
    last_upload_date = args.last_upload_date
    write_last_upload_date_loc = True

if write_last_upload_date_loc:
    try:
        with open(last_upload_date_loc, 'wb') as f:
            pickle.dump(last_upload_date, f)
    except IOError as e:
        print('Error writing to %r' % last_upload_date_loc, file=sys.stderr)
        sys.exit(0)
