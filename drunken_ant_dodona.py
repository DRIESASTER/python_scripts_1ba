# https://dodona.ugent.be/nl/courses/1151/series/12988/activities/276629077
def grid(getal, spoor):
    assert len(spoor)==getal*getal, "invalid arguments"
    nieuweLijst = []
    for i in range(0, len(spoor), getal):
        current = []
        for k in range(i, i + getal):
            current.append(spoor[k])
        nieuweLijst.append(current)
    return nieuweLijst

def text(rooster):
    zin=''
    for i in rooster:
        zin+= ' '.join(i) + '\n'
    return zin[:-1]

def step(vierkant,coord):
    rijNr= coord[0]
    kolomNr= coord[1]
    newCoord= []
    legende= {"^" : ">", ">" : "v", "v" : "<", "<" : "^"}
    rijCounter= {"^" : int(rijNr!=0)*-1, ">" : 0, "v" : int(rijNr!=len(vierkant)-1)*1, "<" : 0}
    kolomCounter = {"^": 0, ">": int(kolomNr!=len(vierkant[0])-1)*1, "v": 0, "<": int(kolomNr!=0)*-1}
    rij= vierkant[rijNr]
    char= vierkant[rijNr][kolomNr]
    vierkant[rijNr][kolomNr]= legende[vierkant[rijNr][kolomNr]]
    newCoord.append(coord[0] + rijCounter[char])
    newCoord.append(coord[1] + kolomCounter[char])
    return tuple(newCoord)

def steps(vierkant):
    pos= (len(vierkant)-1,0)
    coords= [pos]
    while pos != (0,len(vierkant[0])-1):
        pos= step(vierkant,pos)
        coords.append(pos)
    return coords
