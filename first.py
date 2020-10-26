# This is the beginning of my game
from character import character
from scene import getScene
from actionResolution import actionResolution

actionOption = ''
hits = getScene(character.location)

while(actionOption != 'q'):
    getIt = input("What would you like to do? ")
    actionOption = getIt.lower()

    actionResolution(character, actionOption, hits)
