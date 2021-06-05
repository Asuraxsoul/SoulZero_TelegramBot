import math

boulder_gyms = '''
{
    "boulderGyms": [
        { 
        "name": "Z-Vertigo",
        "image": "./database/photos/zVertigoImage.jpg",
        "location": "170 Upper Bukit Timah Rd, #B2-20B, Singapore 588179",
        "lat": 1.3441197332792432,
        "lng": 103.77594945397215,
        "category": "West",
        "url": "https://zvertigobouldergym.wixsite.com/zvert",
        "booking": "https://www.picktime.com/ZVbooking"
        },
        {
        "name": "Boulder World",
        "image": "./database/photos/boulderWorldImage.jpg",
        "location": "10 Eunos Rd 8, #01-205 SingPost Centre (Enrichment Zone), Singapore 408600",
        "lat": 1.3192484369427298,
        "lng": 103.89479204013315,
        "category": "East",
        "url": "https://boulderworld.com/",
        "booking": "https://www.picktime.com/566fe29b-2e46-4a73-ad85-c16bfc64b34b"
        },
        {
        "name": "Test Gym",
        "image": "./database/photos/boulderWorldImage.jpg",
        "location": "10 Eunos Rd 8, #01-205 SingPost Centre (Enrichment Zone), Singapore 408600",
        "lat": 1.346898,
        "lng": 103.731779,
        "category": "East",
        "url": "https://boulderworld.com/",
        "booking": "https://www.picktime.com/566fe29b-2e46-4a73-ad85-c16bfc64b34b"
        }
    ]
}
'''
#
# latitude = 1.3519209524180806
# longitude = 103.69633438912454
#
# # Haversine Formula to calculate distance between 2 lat-lng points
# earth_radius = 6378.0
# within_distance = 5.0
# lat1 = math.radians(latitude)
# lng1 = math.radians(longitude)
#
# lat2 = math.radians(1.3192484369427298)
# lng2 = math.radians(103.89479204013315)
# dlat = lat2 - lat1
# dlng = lng2 - lng1
#
# a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlng / 2) ** 2
# c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
# distance = earth_radius * c
#
# print(distance)
