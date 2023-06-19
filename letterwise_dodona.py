# https://dodona.ugent.be/nl/courses/1151/series/12989/activities/1301698881
import re

def lees_databank(fbestand):
    with open(fbestand, 'r') as bestand:
        databank = {prefix.split(',')[0]: prefix.split(',')[1].replace('\n', '') for idx, prefix in enumerate(bestand)}
    return databank

def letter(prefix,toets,databank):
    regex= ["[^ ]","[^_,@]","[^ABC]","[^DEF]","[^GHI]","[^JKL]","[^MNO]","[^PQRS]","[^TUV]","[^WXYZ]"]
    index= prefix
    if len(prefix)>3:
        index= prefix[len(prefix)-3:]
    if not index in databank.keys():
        index=''
    return (re.sub(regex[int(toets[0])],"", databank[index]))[(len(toets)-1)%(len(regex[int(toets[0])])-3)]

def combinaties(toetsen):
    return (re.sub("([0-9])",r",\1" ,toetsen))[1:].split(",")

def woord(toetsen,databank):
    prefix= ''
    for i in combinaties(toetsen):
        prefix+=letter(prefix,i,databank)
    return prefix