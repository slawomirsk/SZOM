import decimal
import math

import rating
class Student:
    def __init__(self,surname,names,yearOfStuding,number):
        self.surname=surname
        self.names=names
        self.yearOfStuding=yearOfStuding
        self.number=number
        self.ratings=[]
        self.state=""
        self.finalRatings=[]
    def printDate(self):
        print("{} {} {}".format(self.surname, self.names, self.state))
        for r in self.ratings:
            print("{} {} {} {} ".format(r.yearOfStuding, r.modul, r.unit, r.value))

    def printFinalRatings(self):
        print("{} {} {}".format(self.surname, self.names, self.state))
        for r in self.finalRatings:
            print("{} {} {}  ".format(r.yearOfStuding, r.modul, r.value))
    def calculateFinalsRatings(self, net):
        modulsNames=self.__getModulsNames()
        for m in modulsNames:
            self.__calculateFinalsRatingsOfModul(m,net)
    def __getModulsNames(self):
        modulsNames=[]
        for w in self.ratings:
            if modulsNames.count(w.modul)==0 and w.yearOfStuding==self.yearOfStuding:
                modulsNames.append(w.modul)
        return modulsNames

    def __calculateFinalsRatingsOfModul(self, m, net):
        if self.state=="Brak Ocen z poprzednich lat.":
            r= rating.Rating(m, self.yearOfStuding, "Brak Ocen")
            self.finalRatings.append(r)
            return
        ## znajdz nieklasyfikowania
        if self.__FindNK(m):
            r = rating.Rating(m, self.yearOfStuding, "nk")
            self.finalRatings.append(r)
            return
        if self.__FindOne(m):
            r = rating.Rating(m, self.yearOfStuding, 1)
            self.finalRatings.append(r)
            return
        ## oblicz jeśli brak ocen
        if len(self.ratings)==0:
            r = rating.Rating(m, self.yearOfStuding, "-")
            self.finalRatings.append(r)
            return

        if self.yearOfStuding==net.yearOfModulsEnd[m]:
            ratingSum=0
            weightSum=0
            for r in self.ratings:
                if r.modul==m:
                    v=net.getValue(r)
                    ratingSum+=int(r.value)*int(v)
                    weightSum+=int(v)
            goal = 1.0*ratingSum/weightSum
            #r = rating.Rating(m, self.yearOfStuding, round(goal,0))
            r = rating.Rating(m, self.yearOfStuding, self.round_half_up(goal, 0))
            self.finalRatings.append(r)
            return
        else:
            ratingSum = 0
            weightSum = 0
            for r in self.ratings:
                if r.modul == m and r.yearOfStuding==self.yearOfStuding:
                    v = int(net.getValue(r))
                    ratingSum+=int(r.value)*int(v)
                    weightSum += int(v)
            goal = 1.0 * ratingSum / weightSum
            r = rating.Rating(m, self.yearOfStuding, self.round_half_up(goal, 0))
            self.finalRatings.append(r)
            return


        ## oblicz w przeciwnym przypadku

    def round_half_up(self,n, decimals=0):
        multiplier = 10 ** decimals
        return int(math.floor(n * multiplier + 0.5) / multiplier)
    def __FindNK(self, m):
        for w in self.ratings:
            if w.modul==m and w.yearOfStuding == self.yearOfStuding and w.value=="nk":
                return True
        return False

    def __FindOne(self, m):
        for w in self.ratings:
            if w.modul==m and w.yearOfStuding == self.yearOfStuding and w.value==1:
                return True
        return False
    def writeFinalRatings(self):
        surnameName=self.surname+" "
        for n in self.names:
            surnameName=surnameName+" "+n
        s="{:30s}".format(surnameName)
        for r in self.finalRatings:
            s=s+"{}={} |".format(r.modul,r.value)
        s=s+"\n"
        return s


