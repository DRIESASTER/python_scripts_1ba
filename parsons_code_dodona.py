# https://dodona.ugent.be/nl/courses/1151/series/12990/activities/345941930
import re

def maximale_afwijking(lijn):
    min= 0
    max= 0
    current= 0
    lastchar= ""
    lijn= lijn.lower()
    for i in lijn:
        if i=="r":
            i=lastchar
        elif i=="u":
            current+=1
        elif i=="d":
            current-=1
        if current>max:
            max=current
        if current<min:
            min=current
        lastchar=i
    koppel= (min,max)
    return koppel

def parsons(file):
    words = list(str(max(open(file), key=len)))
    with open(file) as textfile:
        lines = textfile.read().splitlines()
        for line in lines:
            for count, el in enumerate(line):
                if el != " ":
                    words[count] = el
    tekst = "*" + "".join(words).replace("*", "").replace("\n", "").replace("/", "U").replace("-", "R").replace("\\","D")
    return tekst

def contour(patroon,file=None):
    patroon= patroon[1:].lower()

    tekening= []
    filler= [" "]
    for i in patroon:
        filler.append(" ")
        if i!="*":
            filler.append(" ")

    for i in range(0,maximale_afwijking(patroon)[0] * -2 + maximale_afwijking(patroon)[1] * 2 + 1):
        tekening.append(filler[::])

    x= 1
    y= maximale_afwijking(patroon)[1] * 2
    tekening[y][0]= "*"

    lastchar= ""
    for i in patroon:

        if i=="r":
            if lastchar=="":
                tekening[y][x]="-"
                tekening[y][x+1]="*"
            elif lastchar=="d":
                tekening[y + 1][x] = "\\"
                tekening[y + 2][x + 1] = "*"
                y += 2
            elif lastchar=="u":
                tekening[y - 1][x] = "/"
                tekening[y - 2][x + 1] = "*"
                y -= 2


        if i=="d":
            tekening[y+1][x]="\\"
            tekening[y+2][x+1]="*"
            y+=2

        if i=="u":
            tekening[y-1][x]="/"
            tekening[y-2][x+1]="*"
            y-=2
        x += 2
    if file is None:
        for i in tekening:
            print("".join(i))
    else:
        with open(file, 'w') as f:
            for i in tekening:
                f.write("".join(i) + "\n")