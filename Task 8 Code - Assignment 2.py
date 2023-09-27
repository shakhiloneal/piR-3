# Import the required modules
from city_data import city_data
from geopy.distance import geodesic
from abc import ABC, abstractclassmethod
import math

class vehicle(ABC):
    def __init__(self, distance):
        pass
    @abstractclassmethod
    def travel_times(self):
        pass

class CrepeCar(vehicle):
    def __init__(self, distance, speed):
        self.distance = distance
        self.speed = speed
    def travel_times(self):
        travelDuration = (math.ceil(self.distance / self.speed))
        return (str(travelDuration) + " hours")

class DonutDinghy(vehicle):
    def __init__(self, distance, domesticSpeed, internationalSpeed):
        self.distance = distance
        self.domesticSpeed = domesticSpeed
        self.internationalSpeed = internationalSpeed   
    def travel_times(self):
        travelDurationDomestic = (math.ceil(self.distance / self.domesticSpeed))
        return (str(travelDurationDomestic) + " hours") 
    def travel_times_international(self):
        travelDurationInternational = (math.ceil(self.distance / self.internationalSpeed))
        return (str(travelDurationInternational) + " hours") 

class TarteTrolley(vehicle):
    def __init__(self, distance):
        self.distance = distance
    def travel_times(self):
        if distance <= 2000:
            travelDuration = "6 hours"
            return travelDuration
        else:
            return "Infinity"
    def travel_times_3000(self):
        if distance <= 3000:
            travelDuration = "8 hours"
            return travelDuration
        else: 
            return "Infinity"

print("""Delivering baked goods to 363 cities.
Bakery vehicles:
 0. Crappy Crepe Car (crappy speed: 250 km/h)
 1. Diplomacy Donut Dinghy (domestic speed: 100 km/h | international speed: 500 km/h)
 2. Diplomacy Donut Dinghy (domestic speed: 50 km/h | international speed: 800 km/h)
 3. Teleporting Tarte Trolley (blink time: 6 h | blink range: 2000 km)
 4. Teleporting Tarte Trolley (blink time: 8 h | blink range: 3000 km)""")

# Obtain ID for departure city and find its location and name
departureInput = int(input("Enter the ID of the departure city:\n"))
for lists in city_data:
    if lists[8] == str(departureInput):
        departureLat = float(lists[1])
        departureLng = float(lists[2])
        departureCapital = lists[6]
        departureCountry = lists[3]
        departureName = lists[0]
        break

# Obtain ID for destination city and find its location and name
destinationInput = int(input("Enter the ID of the destination city:\n"))
for lists in city_data:
    if lists[8] == str(destinationInput):
        destinationLat = float(lists[1])
        destinationLng = float(lists[2])
        destinationCapital = lists[6]
        destinationCountry = lists[3]
        destinationName = lists[0]
        break

# Calculate distance between the cities
point1 = (departureLat, departureLng)
point2 = (destinationLat, destinationLng) 
distance = math.ceil(geodesic(point1, point2).kilometers)

# Calcualte travel time for Crappy Crepe Car
crepeCarTravelTime = CrepeCar(distance, 250).travel_times()

# Calculate travel time for Diplomacy Donut DonutDinghy (Version 1)
if departureCountry == destinationCountry:
    donutDinghyTravelTime1 = DonutDinghy(distance, 100, 500).travel_times()
elif departureCapital == "primary" and destinationCapital == "primary":
    donutDinghyTravelTime1 = DonutDinghy(distance, 100, 500).travel_times_international()
else: 
    donutDinghyTravelTime1 = "Infinity"

# Calculate travel time for Diplomacy Donut DonutDinghy (Version 2)
if departureCountry == destinationCountry:
    donutDinghyTravelTime2 = DonutDinghy(distance, 50, 800).travel_times()
elif departureCapital == "primary" and destinationCapital == "primary":
    donutDinghyTravelTime2 = DonutDinghy(distance, 50, 800).travel_times_international()
else: 
    donutDinghyTravelTime2 = "Infinity"

# Calculate travel time for Teleporting Tarte Trolley (version 1)
tarteTrolleyTravelTime1 = TarteTrolley(distance).travel_times()

# Calculate travel time for Teleporting Tarte Trolley (version 2)
tarteTrolleyTravelTime2 = TarteTrolley(distance).travel_times_3000()

# Print out the results
print(f"Direct travel times from {departureName} to {destinationName}:")
print(f""" 0. {crepeCarTravelTime}
 1. {donutDinghyTravelTime1}
 2. {donutDinghyTravelTime2}
 3. {tarteTrolleyTravelTime1}
 4. {tarteTrolleyTravelTime2}""")

