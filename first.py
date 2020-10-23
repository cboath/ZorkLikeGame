# This is the beginning of my game
from character import character
from scene import getScene
from actionResolution import actionResolution

actionOption = ''

print('You are located at', character.location)

while(actionOption != 'q'):

    hits = getScene(character.location)

    getIt = input("What would you like to do? ")
    actionOption = getIt.lower()

    actionResolution(character, actionOption, hits)
