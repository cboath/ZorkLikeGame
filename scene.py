import json

def getScene(charloc):
    print(charloc)
    if(charloc[0] == 'f'):
        with open('scenelistforest.json') as forest:
            forestloc = json.load(forest)
            print(forestloc)
        
    