# https://dodona.ugent.be/nl/courses/1151/series/12989/activities/534402833
import random
import itertools

aantal= ['een','twee','drie']
vulling= ['vol','halfvol','leeg']
kleur= ['rood','groen','paars']
vorm= ['ruit','golf','ovaal']

def willekeurige_kaart():
    return tuple([random.choice(aantal), random.choice(vulling), random.choice(kleur), random.choice(vorm)])

def willekeurige_kaarten(aantal):
    setje= set()
    counter= 0
    while len(setje)!=aantal:
        setje.add(willekeurige_kaart())
    return setje

def eigenschappen(set1,set2,set3):
    lijst= []
    for i in range(0,4):
        setje= set()
        setje.add(set1[i])
        setje.add(set2[i])
        setje.add(set3[i])
        lijst.append(setje)
    return tuple(lijst)

def isset(kaart1,kaart2,kaart3):
    eig= eigenschappen(kaart1,kaart2,kaart3)
    for i in eig:
        if len(i)==2:
            return False
    return True

def sets(lijst):
    aantal= 0
    lijst= itertools.combinations(lijst,3)
    for i in lijst:
        if isset(i[0],i[1],i[2]):
            aantal+=1
    return aantal