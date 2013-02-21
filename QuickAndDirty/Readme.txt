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

Requires installing:
  fbconsole (for access to facebook - this is the reason I'm not using python 3.2, fbconsole wouldn't install using pip)
  Requests (for the most up-to-date way of handling HTTP in 2013)
  scipi (for statistics so I don't have to reinvent the wheel for a t-test)

$ sudo pip install fbconsole
$ sudo apt-get install python-requests #Default pip installation fails on ubuntu
$ sudo apt-get install python-scipy

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
