class EasterEgg:

    def __init__(self, m, n, paashaas, file):
        self.bord = []
        self.paashaas = [ord(paashaas[0]) - ord("A"), int(paashaas[1:]) - 1]

        for i in range(0,m):
            rij = []
            for k in range(0,n):
                rij.append("#")
            self.bord.append(rij)

        lines = open(file, encoding="UTF-8").read().splitlines()
        self.eidict = {}
        for line in lines:
            rij = ord(line[0]) - ord("A")
            kolom =int(line[1:]) - 1
            self.eidict[(rij, kolom)] = line
            self.bord[rij][kolom] = "O"

    def __repr__(self):
        self.bord[self.paashaas[0]][self.paashaas[1]] = "X"
        bordString = ""
        for i in self.bord:
            bordString+= "".join(i) + "\n"
        return bordString[:len(bordString)-1]

    def isleeg(self):
        return len(self.eidict) == 0

    def eieren(self):
        return set(self.eidict.values())

    def haas(self):
        return chr(self.paashaas[0] + ord("A")) + str(int(self.paashaas[1:][0]) + 1)

    def mogelijke_zettenCoord(self):
        mogelijkePos = []
        x = self.paashaas[1]
        y = self.paashaas[0]
        if x - 2 >= 0:
            if y - 1 >= 0:
                mogelijkePos.append([y - 1, x - 2])
            if y + 1 < len(self.bord):
                mogelijkePos.append([y + 1, x - 2])
        if x + 2 < len(self.bord[0]):
            if y - 1 >= 0:
                mogelijkePos.append([y - 1, x + 2])
            if y + 1 < len(self.bord):
                mogelijkePos.append([y + 1, x + 2])
        if y - 2 >= 0:
            if x - 1 >= 0:
                mogelijkePos.append([y - 2, x - 1])
            if x + 1 < len(self.bord[0]):
                mogelijkePos.append([y - 2, x + 1])
        if y + 2 < len(self.bord):
            if x - 1 >= 0:
                mogelijkePos.append([y + 2, x - 1])
            if x + 1 < len(self.bord[0]):
                mogelijkePos.append([y + 2, x + 1])
        for pos in range(x + 1, len(self.bord[0])):
            mogelijkePos.append([y, pos])
        return mogelijkePos

    def mogelijke_zetten(self):
        mogelijkePos = self.mogelijke_zettenCoord()
        mogelijk = set()
        for zet in mogelijkePos:
            mogelijk.add(chr(zet[0] + ord("A")) + str(int(zet[1:][0]) + 1))
        return mogelijk

    def zet(self, vak):
        mogelijkePos = self.mogelijke_zettenCoord()

        rij = ord(vak[0]) - ord("A")
        kolom = int(vak[1:]) - 1
        vak = [rij,kolom]
        assert(vak in mogelijkePos), "ongeldige zet"
        if self.bord[rij][kolom] == "O":
            del self.eidict[(rij, kolom)]
        self.bord[self.paashaas[0]][self.paashaas[1]] = "#"
        self.paashaas = vak[:]
        return self