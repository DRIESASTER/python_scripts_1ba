# https://dodona.ugent.be/nl/courses/1151/series/12991/activities/747849983
class Rechthoek():
    r= 0
    k= 0
    h= 0
    b= 0
    def __init__(self, r, k, h, b=0):
        if b == 0:
            b= h
        self.r= r
        self.k= k
        self.h= h
        self.b= b

    def __repr__(self):
        return "Rechthoek(" + str(self.r) + ", " + str(self.k) + ", " + str(self.h) + ", " + str(self.b) + ")"

    def oppervlakte(self):
        return self.h * self.b

    def cellen(self):
        coord = set()
        for i in range(0,self.h):
            for k in range(0,self.b):
                coord.add(((i+self.r),(k+self.k)))
        return coord

    def __le__(self, other):
        for cell in self.cellen():
            if cell not in other.cellen():
                return False
        return True

    def __and__(self, other):
        lijst = []
        for cell in self.cellen():
            if cell in other.cellen():
                lijst.append(cell)
        if len(lijst) == 0:
            return None
        lijst = sorted(lijst, key=lambda x: (x[1],x[0]))
        h= lijst[len(lijst)-1][0] - lijst[0][0] + 1
        b= lijst[len(lijst)-1][1] - lijst[0][1] + 1
        return Rechthoek(lijst[0][0],lijst[0][1], h, b)



class Shikaku():

    def __init__(self,file):
        self.file = file
        lines = open(self.file, encoding= "UTF-8").read().splitlines()[1:]
        self.coord = []
        self.value = {}
        self.cellDict = {}
        self.rechthoeken= []
        self.breedte = int(open(self.file).read().splitlines()[0].split(" ")[0])
        self.hoogte = int(open(self.file).read().splitlines()[0].split(" ")[1])
        for line in lines:
            line = [int(x) for x in (line.split(" "))]
            temp = []
            self.cellDict[tuple(line[:2])] = False
            self.value[tuple(line[:2])] = line[2]
            for i in line:
                temp.append(int(i))
            self.coord.append(temp)



    def cellen(self, rechthoek):
        lijst = []
        for i in rechthoek.cellen():
            for k in range(0, len(self.coord)):
                if list(i) == self.coord[k][:2]:
                    lijst.append(i)
        return lijst

    def getallen(self, rechthoek):
        lijst= []
        for i in self.cellen(rechthoek):
            val= ((i[0],i[1]))
            lijst.append(self.value[val])
        return lijst

    def onbedekt(self):
        return set([x for x in self.cellDict if self.cellDict[x] == False])


    def isopgelost(self):
        for i in self.cellDict:
            if self.cellDict[i] == False:
                return False
        return True

    def bedekken(self, rechthoek):

        for rhoek in self.rechthoeken:
            assert(rechthoek.cellen() != rhoek.cellen()), "ongeldige rechthoek"


        for cell in rechthoek.cellen():
            assert(cell[0] < self.breedte and cell[1] < self.hoogte), "ongeldige rechthoek"
        counter= 0
        for cell in rechthoek.cellen():
            if cell in self.cellDict:
                counter+=1
        assert(counter == 1), "ongeldige rechthoek"
        for cell in rechthoek.cellen():
            if cell in self.cellDict:
                self.cellDict[cell] = True
        self.rechthoeken.append(rechthoek)

    def verwijderen(self, coord):
        bool = False
        assert(coord in self.cellDict), "ongeldige positie"
        assert(self.cellDict[coord] == True), "ongeldige positie"
        self.cellDict[coord] = False

        for rechthoek in self.rechthoeken:
            if coord in rechthoek.cellen():
                self.rechthoeken.remove(rechthoek)









if __name__ =='__main__':
    print(Rechthoek(8, 0, 2, 6) & Rechthoek(4, 2, 7, 5))


