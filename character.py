import json

with open('savedchar.json') as charsheet:
    data = json.load(charsheet)

class character:
    location = data['location']
    inventory = data['inventory']
