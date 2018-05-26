Requirements:
- Python 3
- Requests: the requests module may not be included in Python 3 by default.
To install requests:
$ pip3 install requests
Or manually at https://pypi.org/project/requests/


To run via command line:
$ python3 main.py
[enter command line switches/parameters here]

The following command line switches/parameters are supported:
--help : prints a help message
--synopsis : prints a brief description of the program
-location="enter location here" : user enters the location for which they want the information of
--bat=STRING : does nothing
-s email@domain.com : sends an email of the location information to email@domain.com

To finish entering switches/parameters, enter ".eot"

You may put all switches/parameters on the same line:
$ python3 main.py
--help --synopsis -location="disneyland" -s email@domain.com .eot

Or put each one on a separate line:
$ python3 main.py
--help
--synopsis
-location="UCSD"
-s email@domain.com
.eot

The program will function the same either way.
