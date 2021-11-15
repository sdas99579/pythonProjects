import phonenumbers
#from myNumber import  numbers
from phonenumbers import timezone,geodata,geocoder,length_of_geographical_area_code,carrier,carrierdata
#from opencage.geocoder import OpenCageGeocode

import geopy
from geopy.geocoders import Nominatim
from pprint import pprint
number = input("Enter your number with country code: -  ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone,"en")
reg = geocoder.description_for_number(phone,"en")
#len = length_of_geographical_area_code(phone,"en")

#data = phonenumbers.carrierdata.CARRIER_DATA.get(phone)


print(phone)
print('timezone: ', time)
print(f'Service Provider: ', car)
print(f'Location: ',reg)
#print(len)
#print(data)
'''
app = Nominatim(user_agent="phone")
location = app.geocode(phone)
pprint(location)

'''