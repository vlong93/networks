import requests
 
URL = "http://maps.googleapis.com/maps/api/geocode/json"
 
location = "cal poly pomona"
 
PARAMS = {'address':location}
 
r = requests.get(url = URL, params = PARAMS)
 
data = r.json()
 
latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']
formatted_address = data['results'][0]['formatted_address']
 
print("Latitude: %s\nLongitude: %s\nAddress: %s"
      %(latitude, longitude,formatted_address))