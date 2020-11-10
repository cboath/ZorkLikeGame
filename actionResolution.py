from scene import getScene
from take import take

# Resolve movement
def move(direction, character, hits):
    # Valid directions
    possDirec = hits['directions']
    firstDirec = direction[0]

    # If not a valid direction
    while firstDirec not in possDirec:
        print('Where to? ', possDirec)
        testDir = input('Not a valid direction.  Which way would you like to go? ')
        firstDirec = testDir[0].lower()

    if(firstDirec == 'n'):
        character.location[1] += 1
    if(firstDirec == 's'):
        character.location[1] -= 1
    if(firstDirec == 'e'):
        character.location[2] += 1
    if(firstDirec == 'w'):
        character.location[2] -= 1

    hits = getScene(character.location)

    return hits


def examine(character, action, hits):
    # if there is only one item in action it is likely examine and will return the text describing the location
    if(len(action) == 1):
        hits = getScene(character.location)
    else:
        print(hits['sign'])


def actionResolution(character, actionOption, hits):

    if actionOption in ('q', 'quit'):
        return
    
    if(len(actionOption) > 1):      
        action = actionOption.split()
        if action[0] in ('go', 'move', 'walk'):
            move(action[1], character, hits)
        if action[0] in ('read', 'examine'):
            examine(character, action, hits)
        if action[0] in ('take', 'grab'):
            take(character, action, hits)

    else:
        move(actionOption, character, hits)
