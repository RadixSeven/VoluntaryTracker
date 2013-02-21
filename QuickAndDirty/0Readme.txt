------------------------------------------------------------------------------
Simple idea
-----------

command-line client that downloads all days since last download from
fogbugz, parses the result and uploads them to facebook as fbconsole
program.

Python pickle file holds: username, password, and last download date
Pickle file will not be stored in the repo.

Write simple second command line to fill the pickle file

Run at log-in.

------------------------------------------------------------------------------
Dependencies
------------

I've written things using python 2.7

Requires installing fbconsole (for access to facebook) and Requests (for the current way of handling HTTP

$ sudo pip install fbconsole
$ sudo apt-get install python-requests #Default pip installation fails on ubuntu

------------------------------------------------------------------------------
Important improvements to make it useful to others
--------------------------------------------------

Use a different app id for facebook

Have the program learn last upload date by doing a query from facebook
(thus the program will work even when run on different computers).



------------------------------------------------------------------------------
Other improvements
------------------

Improve the uploaded data: break out times uploaded by project. 

Graph time usage over a given time period (time spent over the last week).
