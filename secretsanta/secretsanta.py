import random

def getNames():
    print("Who are the people participating in Secret Santa this year?")
    print("Please separate each name by commas")
    asString = input()
    asString = asString.lower()
    names = asString.split(", ")
    return names

def isEmpty(string):
    empty1 = ""
    empty2 = " "
    if string == empty1 or string == empty2:
        return True
    return False

def getCouples():
    print("Who are the couples in the group?")
    asString = input("Please list couples as: name1 and name2, name3 and name4\n")
    if isEmpty(asString):
        return [{},{}]
    asString = asString.lower()
    asList = asString.split(", ")
    asPairs = asList
    for s in range(len(asPairs)):
        asPairs[s] = asPairs[s].split(" and ")
    map1 = {}
    for s in range(len(asPairs)):
        map1[asPairs[s][0]] = asPairs[s][1]
    map2 = {}
    for key in map1:
        map2[map1[key]] = key
    coupleMap = [map1,map2]
    return coupleMap

def isCouple(name1, name2, coupleMap):
    map1 = coupleMap[0]
    map2 = coupleMap[1]
    if name1 in map1 and map1[name1] == name2:
        return True
    if name2 in map2 and map2[name2] == name2:
        return True
    return False

def nameCap(name):
    return name[0].upper() + name[1:]

def spaceOut():
    print("=====================================================================")

def main():
    print()
    spaceOut()
    names = getNames()
    spaceOut()
    if isEmpty(names):
        print("There are no participants!")
        spaceOut()
        return
    coupleMap = getCouples()
    spaceOut()
    done = []
    mapOut = {}
    leftOut = "NA"
    if len(names)%2 != 0:
        leftOut = random.choice(names)
        done.append(leftOut)
    for i in range(len(names)):
        if names[i] in done:
            continue
        partner = random.choice(names)
        while names[i] == partner or partner in done or isCouple(names[i], partner, coupleMap):
            partner = random.choice(names)
        mapOut[names[i]] = partner
        done.append(names[i])
        done.append(partner)
    print("Here are the pairs:")
    for key in mapOut:
        print(nameCap(key) + ": " + nameCap(mapOut[key]))
    if leftOut != "NA":
        print(nameCap(leftOut) + ": " + "Unfortunately, " + nameCap(leftOut) + " could not be assigned a partner")
    spaceOut()
    print()

main()
