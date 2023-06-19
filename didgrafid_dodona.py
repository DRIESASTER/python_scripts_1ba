# https://dodona.ugent.be/nl/courses/1151/series/12991/activities/1130089622
class Rooster():

    sleutel = ""
    rooster = []
    alphabet = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def __init__(self, sleutel):
        self.rooster = []
        sleutel = sleutel.upper()

        self.sleutel = sleutel
        sleutelWaarden = []

        for char in sleutel:
            if char not in sleutelWaarden:
                sleutelWaarden.append(char)

        for char in self.alphabet:
            if char not in sleutelWaarden:
                sleutelWaarden.append(char)

        sleutelWaarden = list(sleutelWaarden)
        counter = 0
        for i in range(0,3):
            lst = []
            for k in range(0,9):
                lst.append(sleutelWaarden[counter])
                counter+=1
            self.rooster.append(lst)

    def positie(self, char):
        char = char.upper()
        y= 0
        for i in range(0,3):
            x= 0
            for k in range(0,9):
                if self.rooster[y][x] == char:
                    return y,x
                x+=1
            y+= 1

    def __repr__(self):
        value=""
        for i in self.rooster:
            value+= ("".join(i))+ "\n"
        return (value[:len(value)-1])

    def karakter(self,r,k):
        return self.rooster[r][k]


class Digrafid():
    rooster1 = None
    rooster2 = None

    def __init__(self, sleutel1, sleutel2):
        self.rooster1 = Rooster(sleutel1)
        self.rooster2 = Rooster(sleutel2)

    def triplet(self, string):
        char1= string[0]
        coord1=self.rooster1.positie(char1)

        char2= string[1]
        coord2=self.rooster2.positie(char2)

        return ((coord1[1], (3*coord1[0]+coord2[0]), coord2[1]))

    def digraaf(self,g1,g2,g3):
        woord= ""
        woord+= self.rooster1.karakter((g2//3),g1)
        woord+= self.rooster2.karakter((g2%3),g3)
        return woord

    def codeer(self,text, codeer=True):
        gecodeerd= ""
        if codeer:
            text+= "X"*((6 - len(text))%6)

        text= [text[i:i+6] for i in range(0, len(text), 6)]
        for part in text:
            part= [part[i:i+2] for i in range(0, len(part), 2)]
            gecodeerd+= self.digraaf(self.triplet(part[0])[0], self.triplet(part[1])[0], self.triplet(part[2])[0])
            gecodeerd += self.digraaf(self.triplet(part[0])[1], self.triplet(part[1])[1], self.triplet(part[2])[1])
            gecodeerd += self.digraaf(self.triplet(part[0])[2], self.triplet(part[1])[2], self.triplet(part[2])[2])
        return gecodeerd

    def decodeer(self, text):
        return self.codeer(text)






if __name__ =='__main__':
    rooster = Rooster("ANNAKIN SKYWALKER")
    dig = Digrafid("Annakin Skywalker", "Padme Amidala")
    print(dig.decodeer('SEOMHFGLAPFXJCAMXW PHLCYFFKBK EZFRE JJCPTEYOGZTI'))
