Requirements:
- Python 3
- Requests: the requests module may not be included in Python 3 by default.
To install requests:
$ pip3 install requests
Or manually at https://pypi.org/project/requests/


To run via command line:
$ python3 main.py
[enter command line switches/parameters here]

The following command line switches/parameters are supported:<br>
--help : prints a help message<br>
--synopsis : prints a brief description of the program<br>
-location="enter location here" : user enters the location for which they want the information of<br>
--bat=STRING : does nothing<br>
-s email@domain.com : sends an email of the location information to email@domain.com<br>

To finish entering switches/parameters, enter ".eot"

You may put all switches/parameters on the same line:<br>
$ python3 main.py<br>
--help --synopsis -location="disneyland" -s email@domain.com .eot<br>

Or put each one on a separate line:<br>
$ python3 main.py<br>
--help<br>
--synopsis<br>
-location="UCSD" <br>
-s email@domain.com <br>
.eot<br>

The program will function the same either way.
