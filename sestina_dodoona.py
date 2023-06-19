# https://dodona.ugent.be/nl/courses/1151/series/12990/activities/678203984
import re

def eindwoord(lijn):
    return re.sub("^.*[^a-zA-Z]([a-zA-Z]+)[^a-zA-Z]*$", r"\1" ,lijn)

def stanzas(file):
    lijst= []
    with open(file) as textfile:
        lines = textfile.read().splitlines()
        temp= []
        for line in lines:
            if line != "":
                temp.append(eindwoord(line).lower())
            else:
                if len(temp) > 0:
                    lijst.append(temp)
                temp= []
        lijst.append(temp)
    return lijst

def permutatie(lijst, patroon = None):
    #canonieke patroon bepalen
    if patroon is None:
        patroon= []
    if len(patroon) == 0:
        for i in range(0,len(lijst)//2):
            patroon.append(len(lijst)-i)
            patroon.append(i+1)
        if len(lijst)%2 != 0:
            patroon.append(len(lijst)//2+1)

    #assertions
    assert len(set(patroon)) == len(lijst), "ongeldige permutatie"
    assert all([el != 0 for el in patroon]), "ongeldige permutatie"
    test= 0
    test2= 0
    for i in range(0,len(patroon)):
        test+= i
    for i in patroon:
        test2+=i-1
    assert (test == test2), "ongeldige permutatie"

    #effectieve permutatie uitvoeren
    lijst2= []
    for i in patroon:
        lijst2.append(lijst[i-1])
    return lijst2

def sestina(file, patroon= None):
    gedicht = stanzas(file)
    
    if len(gedicht) == len(gedicht[0]) + 1:
        if len(gedicht[-1]) != len(gedicht[0]) // 2:
            return False
        for el in gedicht[-1]:
            if el not in gedicht[0]:
                return False
        for i in range(0, len(gedicht)- 2):
            if permutatie(gedicht[i], patroon) != gedicht[i + 1]:
                return False
        return True
    
    elif len(gedicht) == len(gedicht[0]):
        for i in range(0, len(gedicht)-1):
            if permutatie(gedicht[i], patroon) != gedicht[i+1]:
                return False
        return True

    return False
