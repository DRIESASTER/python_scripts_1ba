# https://dodona.ugent.be/nl/courses/1151/series/12988/activities/70570533
import re
def crossSection(getal, lijn):

    assert (len(lijn)/getal)%2 == 0, "invalid cross section"
    lijst= []
    for i in range(0,getal):
        begin= i*(len(lijn)//getal)
        eind= begin+(len(lijn)//getal)
        zin= lijn[begin:eind]
        lijst2= []
        for k in range(0,len(zin),2):
            lijst2.append(zin[k:k+2])
        lijst.append(lijst2)
    return lijst


def depth(lijst):
    lijst = fixNotatie(lijst)
    matchedLeft = {"NS":"...", "NE":"...", "NW":".*E.*", "SE":"...", "SW":".*E.*", "EW":".*E.*$"}
    matchedRight= {"NS":"...", "NE":".W$", "NW":"...", "SE":".W$", "SW":"...", "EW":".W"}
    matchedUp= {"NS":".*S.*", "NE":".*S.*", "NW":".*S.*","SE":"...","SW":"...", "EW":"..."}
    matchedDown = {"NS": ".*N.*", "NE": "...", "NW": "...", "SE": "N.", "SW": "N.*", "EW":"..."}
    rij = 0
    kolom = 0
    diepte = 0

    last = ''

    while not rij == len(lijst) and not kolom == len(lijst[0]):
        currentLeft = matchedLeft[lijst[rij][kolom]]
        currentRight = matchedRight[lijst[rij][kolom]]
        currentUp = matchedUp[lijst[rij][kolom]]
        currentDown = matchedDown[lijst[rij][kolom]]
        if(kolom+1 < len(lijst[0]) and re.match(currentRight,lijst[rij][kolom+1]) and not last == 'right'):
            kolom+=1
            diepte+=1
            last= 'left'
        elif(kolom-1 >= 0 and re.match(currentLeft,lijst[rij][kolom-1]) and not last == 'left'):
            kolom-=1
            diepte+=1
            last= 'right'
        elif(rij-1 >=0 and re.match(currentUp,lijst[rij-1][kolom]) and not last == 'up'):
            rij-=1
            diepte+=1
            last= 'down'
        elif(rij+1 < len(lijst) and re.match(currentDown,lijst[rij+1][kolom]) and not last == 'down'):
            rij+=1
            diepte+=1
            last= 'up'
        else:
            break

    return diepte+1




def fixNotatie(lijst):
    correcteNotatie= {'WS':"SW","ES":"SE","SN":"NS","WN":"NW","EN":"NE","WE":"EW"}
    for i in range(0,len(lijst)):
        for k in range(0,len(lijst[0])):
            if lijst[i][k] in correcteNotatie:
                lijst[i][k]= correcteNotatie[lijst[i][k]]
    return lijst