#This is the beginning of my game
from character import character
from scene import getScene

print('You are located at', character.location)

getScene(character.location)
#print(scene.description)