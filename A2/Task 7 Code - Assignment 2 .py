# Import the required modules
from city_data import city_data
from geopy.distance import geodesic
import math

# Obtain ID for departure city and find its location and name
print("Delivering baked goods to 363 cities.")
departureInput = int(input("Enter the ID of the departure city:\n"))
for lists in city_data:
    if lists[8] == str(departureInput):
        departureLat = float(lists[1])
        departureLng = float(lists[2])
        departureName = lists[0]
        break

# Obtain ID for destination city and find its location and name
destinationInput = int(input("Enter the ID of the destination city:\n"))
for lists in city_data:
    if lists[8] == str(destinationInput):
        destinationLat = float(lists[1])
        destinationLng = float(lists[2])
        destinationName = lists[0]
        break

# Calculate distance between the cities
point1 = (departureLat, departureLng)
point2 = (destinationLat, destinationLng) 
distance = math.ceil(geodesic(point1, point2).kilometers)

# Print out the results
print(f"Distance between {departureName} and {destinationName}:")
print(f"{distance} km")
