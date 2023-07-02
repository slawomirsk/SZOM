import weight
class Net:
    def __init__(self,address):
        self.yearOfModulsEnd={}
        f=open(address)
        self.weights=[]
        lines=f.readlines();
        for l in lines:
            modul=l[7:9]
            przedmiot=l[10:12]
            lsplit=l.split()
            for i in range(5):
                rok=i+1
                wagaOceny=lsplit[i+1]
                if wagaOceny!="0":
                    w=weight.Weight(modul,przedmiot,rok,wagaOceny)
                    self.weights.append(w)
        f.close()
        for w in self.weights:
            try:
                max=int(self.yearOfModulsEnd[w.modul])
                if max<int(w.yearOfStuding):
                    self.yearOfModulsEnd[w.modul]=int(w.yearOfStuding)
            except:
                self.yearOfModulsEnd[w.modul] = int(w.yearOfStuding)



    def getValue(self, o):
        for w in self.weights:
            if w.modul==o.modul and w.unit[1] == o.unit[1] and  int(w.yearOfStuding)== int(o.yearOfStuding):
                return w.value
