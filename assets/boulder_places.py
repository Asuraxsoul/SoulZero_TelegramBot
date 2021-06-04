import json

boulder_places = '''
{
    "boulderGyms": [
        {
        "name": "Z-Vertigo",
        "image": "./photos/zVertigoImage.jpg",
        "location": "170 Upper Bukit Timah Rd, #B2-20B, Singapore 588179",
        "preciseLocation": 588179,
        "category": "West",
        "url": "https://zvertigobouldergym.wixsite.com/zvert",
        "booking": "https://www.picktime.com/ZVbooking"
        },
        {
        "name": "Boulder World",
        "image": "./photos/boulderWorldImage.jpg",
        "location": "10 Eunos Rd 8, #01-205 SingPost Centre (Enrichment Zone), Singapore 408600",
        "preciseLocation": 408600,
        "category": "East",
        "url": "https://boulderworld.com/",
        "booking": "https://www.picktime.com/566fe29b-2e46-4a73-ad85-c16bfc64b34b"
        }
    ]
}
'''

# all_boulder_places = json.loads(boulder_places)
# print(all_boulder_places)
#
# for gym_info in all_boulder_places['boulderGyms']:
#     print(gym_info['category'])
