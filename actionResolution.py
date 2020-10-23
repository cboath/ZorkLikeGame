import json

# Resolve movement
def move(direction, character, hits):
    # Valid directions
    possDirec = hits['directions']
    firstDirec = direction[0]

    # If not a valid direction
    while firstDirec not in possDirec:
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

def examine(action, hits):
    if(len(action) == 1):
        return
    else:
        print(hits['sign'])


def actionResolution(character, actionOption, hits):

    if actionOption in ('q', 'quit'):
        return
    
    if(len(actionOption) > 1):      
        action = actionOption.split()
        if action[0] in ('go', 'move', 'walk'):
            print('Whahahaha? ', action[0])
            move(action[1], character, hits)
        if action[0] in ('read', 'examine'):
            examine(action, hits)

    else:
        move(actionOption, character, hits)
