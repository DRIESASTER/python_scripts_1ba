import math


class Quaternion():

    def __init__(self,a=0,b=0,c=0,d=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.lijst = [self.a, self.b, self.c, self.d]

    def norm(self):
        return math.sqrt(self.a ** 2 + self.b ** 2 + self.c ** 2 + self.d **2)

    def __str__(self):
        stringValue = str(self.a)
        lijst = [self.b,self.c,self.d]
        varLijst = ["i","j","k"]
        for el in lijst:
            posneg = "+"
            if el<0:
                posneg = "-"
                el = -1 * el
            stringValue+= " " + posneg + " " + str(el) + varLijst[0]
            varLijst.remove(varLijst[0])
        return stringValue

    def __repr__(self):
        lijst = [str(self.a),str(self.b),str(self.c),str(self.d)]
        return  "Quaternion" + "(" + ", ".join(lijst) + ")"

    def __add__(self, other):
        if isinstance(other, Quaternion):
            a = self.a + other.a
            b = self.b + other.b
            c = self.c + other.c
            d = self.d + other.d
        else:
            a = self.a + other
            b = self.b
            c = self.c
            d = self.d
        return Quaternion(a,b,c,d)

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, Quaternion):
            comb = []
            for el in self.lijst:
                comb.append([el * x for x in other.lijst])
            a= comb[0][0]
            for i in range(1,len(comb)):
                a-= comb[i][i]
            b = comb[0][1] + comb[1][0] + comb[2][3] - comb[3][2]
            c = comb[0][2] - comb[1][3] + comb[2][0] + comb[3][1]
            d = comb[0][3] + comb[1][2] + -comb[2][1] + comb[3][0]
        else:
            a = self.a * other
            b = self.b * other
            c = self.c * other
            d = self.d * other
        return Quaternion(a,b,c,d)

    def __rmul__(self, other):
        return self * other