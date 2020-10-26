def take(character, action, hits):
    itemsToTake = hits["items"]

    if(len(action) == 1):
        fleek = input("What would you like to take? ")
        action.append(fleek)
        print("Beeb: ", action)

    print("Things: ", itemsToTake)
