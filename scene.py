import json


def getScene(charloc):
    print(charloc)
    currentloc = [charloc[1], charloc[2]]
    if(charloc[0] == 'f'):
        with open('scenelistforest.json') as forest:
            forestloc = json.load(forest)
            for key, value in forestloc.items():
                for m in range(0, len(value)):
                    if(value[m]['location'] == currentloc):
                        print(value[m]['description'])
