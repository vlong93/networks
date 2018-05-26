import requests
import smtplib
import re
import argparse
 
URL = "http://maps.googleapis.com/maps/api/geocode/json"
server = smtplib.SMTP('smtp.gmail.com', 587)

# user_input = ""
# while ".eot" not in user_input:
# 	user_input += (input() + " ")

# if "--help" in user_input:
# 	print("""
# 		main  [--function] [--bat=token] | --help | --synopsis

# 		This program returns the address and latitude/longitude coordinates 
# 		of a given location.

# 		Version      : 1.0.0
# 		Dependencies : 'requests', 'smtplib', and 're'
# 		Authors      : Jinjing Lee, Vivian Long
# 		Contact      : cs380project1@gmail.com

# 		""")

# if "--synopsis" in user_input:
# 	print(""" Synopsis:
# 		Gets the address and latitude/longitude coordinates of a given location 
# 		and gives the user the option to email this data through G-mail.
# 		""")

input()
parser = argparse.ArgumentParser()
parser.add_argument('--synopsis', help='brief description')
parser.add_argument('-l', action='store', dest='loc', help='enter a location to search', type=str)
args = parser.parse_args()
print(args.loc)


# TODO: add ability to take user input for location
location = "cal poly pomona"


# Searches location data 
PARAMS = {'address':location}
r = requests.get(url = URL, params = PARAMS)
data = r.json()
 
try:
	latitude = data['results'][0]['geometry']['location']['lat']
	longitude = data['results'][0]['geometry']['location']['lng']
	formatted_address = data['results'][0]['formatted_address']

	print("Latitude: %s\nLongitude: %s\nAddress: %s"
	      % (latitude, longitude,formatted_address))
	print()
except:
	print("Invalid location input")


# Handles e-mailing
# recipient = re.search(r'[\w\.-]+@[\w\.-]+', user_input)
# if recipient != None:
# 	server.ehlo()
# 	server.starttls()
# 	server.login("cs380project1@gmail.com", "HelloWorld!")
# 	msg = "This is a test message." 
# 	server.sendmail("cs380project1@gmail.com", recipient[0], msg)
# 	server.close()
# 	print("E-mail successfully sent to", recipient[0])