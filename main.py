import requests
import smtplib
import re
 
URL = "http://maps.googleapis.com/maps/api/geocode/json"
server = smtplib.SMTP('smtp.gmail.com', 587)

user_input = ""
while ".eot" not in user_input:
	user_input += (input() + " ")

if "--help" in user_input:
	print(""" Help:
		main.py  [--function] [--bat=token] [-location=" "] | --help | --synopsis

		This program returns the address and latitude/longitude coordinates 
		of a given location. If no location is specified, the location defaults
		to Cal Poly Pomona.
		
		To send the location information by e-mail, specify an e-mail address.

		Version      : 1.0.0
		Dependencies : 'requests', 'smtplib', and 're'
		Authors      : Jinjing Lee, Vivian Long
		Contact      : cs380project1@gmail.com

		""")

if "--synopsis" in user_input:
	print(""" Synopsis:
		Gets the address and latitude/longitude coordinates of a given location 
		and gives the user the option to email this data through Gmail.
		""")

if "-location=" in user_input:
	location = re.search(r'"(.*?)"', user_input)[0]
else:
	print("No location entered. Default location = Cal Poly Pomona")
	location = "Cal Poly Pomona"


# Searches location data 
PARAMS = {'address':location}
r = requests.get(url = URL, params = PARAMS)
data = r.json()
 
try:
	latitude = data['results'][0]['geometry']['location']['lat']
	longitude = data['results'][0]['geometry']['location']['lng']
	address = data['results'][0]['formatted_address']

	print("The location of", location, "is")
	print("Latitude: %s\nLongitude: %s\nAddress: %s"
	      % (latitude, longitude, address))
	print()

	# Handles e-mailing
	recipient = re.search(r'[\w\.-]+@[\w\.-]+', user_input)
	if recipient is not None:
		server.ehlo()
		server.starttls()
		server.login("cs380project1@gmail.com", "HelloWorld!")
		msg = "\r\n".join([
			"From: Vivian and Jinjing",
			"To: You",
			"Subject: Location",
			"",
			"The location of " + str(location) + " is:",
			"Latitude: %s\nLongitude: %s\nAddress: %s"
			% (latitude, longitude, address)
		])
		server.sendmail("cs380project1@gmail.com", recipient[0], msg)
		server.close()
		print("E-mail successfully sent to", recipient[0])
except Exception as e:
	print("Invalid location input")