"""
This code research nearby places in a given area.
The code is divided in two parts :
    A first part, which uses Google API Geocode,
    tries to lookup the latitude and longitude of
    the place name the user enters.
    The Second part, which uses Google Web services API,
    uses the coordinates retrieved in the first step
    and try to find a certain type of places within a specified range
    associated with a keyword
"""

import urllib
import json
import time

address = raw_input('Enter location: ') # Eg : a city name
range = raw_input('Enter range: ')  # Distance in meter
type = raw_input('Search interest: ') # Can be restaurant, church, etc
keyword = raw_input('Enter keyword: ') # Any

# Geocode API Part
geo_url = 'http://maps.googleapis.com/maps/api/geocode/json?'
# if len(address) < 1 : break
url = geo_url + urllib.urlencode({'sensor':'false','address': address})
print ('Retrieving', url)
uh = urllib.urlopen(url)
data = uh.read()
print ('Retrieved',len(data),'characters')
try: js = json.loads(str(data))
except: js = None

if 'status' not in js or js['status'] != 'OK':
   print ('==== Failure To Retrieve ====')
   print (data)
else:
    print (json.dumps(js, indent=4))
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print ('lat',lat,'lng',lng)
    location = js['results'][0]['formatted_address']
    print (location)

# Web services API Part

place_url = 'https://maps.googleapis.com/maps/api/place/\
nearbysearch/json?'

# For radar search one can use
# https://maps.googleapis.com/maps/api/place/radarsearch/json?parameters

# Set your Google API key
API_key = "Paste Your key string"
url = place_url + urllib.urlencode({\
    'location' : '{},{}'.format(lat,lng),\
    'radius' : range, 'type' : type, 'keyword' : keyword, \
    'key' : API_key})
    # Remember to insert your own key

# Fix duplication with a Do while loop
print ('Retrieving', url)
uh = urllib.urlopen(url)
data = uh.read()
print ('Retrieved',len(data),'characters')
try: js = json.loads(str(data))
except: js = None
if 'status' not in js or js['status'] != 'OK':
   print('==== Failure To Retrieve ====')
   print(data)
else:
   with open("{}_dumps.json".format(address), "w") as dump:
       dump.write(json.dumps(js, indent=4))


       while 'next_page_token' in js:
           print('More pages to retrieve')
           print('....')
           # Pause to account for google limits per second/
           time.sleep(5)
           next_page_url = place_url + urllib.urlencode({\
           'pagetoken' : js['next_page_token'],\
           'key' : API_key})
           # Remember to insert your own key
           print ('Retrieving more at :')
           print (next_page_url)
           more_uh = urllib.urlopen(next_page_url)
           more_data = more_uh.read()
           print ('Retrieved',len(more_data),'more characters')
           try: js = json.loads(str(more_data))
           except: js = None
           if 'status' not in js or js['status'] != 'OK':
              print('==== Failure To Retrieve ====')
              print(more_data)
              break
           else:
               with open("{}_dumps.json".format(address), "a") as dump:
                   dump.write(json.dumps(js, indent=4))
