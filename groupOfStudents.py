from re import sub

from PyPDF2 import PdfReader
from student import Student
from net import Net
import rating
import re



class GroupOfStudents:
    def __init__(self, prefix, yearOfStuding):
        self.prefix = prefix
        self.yearOfStuding = yearOfStuding
        self.students=[]
        self.net=Net(self.prefix+"siatka.txt")
        self.__readListOfStudents(yearOfStuding)
        self.__readDegrees(yearOfStuding)

    def __readDegrees(self,year):
        reader = PdfReader(self.prefix + 'o' + str(year) + '.pdf')
        for p in reader.pages:
            text = p.extract_text()
            text = text.split("\n")
            if self.__isItAModul(text[1]):
                subjectName=text[1]
                subjectName=subjectName.split(" ")
                subjectName=subjectName=subjectName[-1]
                subjectName=subjectName.split(".")
                ocuupation=subjectName[0]
                module=subjectName[1]
                unit=subjectName[2]
                for t in text:
                    if self.__isItARating(t):
                        number=t.split(" ")[0]
                        r=self.__readARating(t)
                        ur=rating.UnitsRating(module,unit,year,r)
                        for s in self.students:
                            if s.number==int(number):
                                s.ratings.append(ur)
                                ##################

    def __readListOfStudents(self,year):
        reader = PdfReader(self.prefix + 'l' + str(year) + '.pdf')
        page = reader.pages[0]
        text = page.extract_text()
        text = text.split("\n")
        for i in range(2, len(text)):
            row = text[i].split(" ")
            if len(row) > 1:
                number = int(row[0])
                surname = row[1]
                names = row[2:]
                s = Student(surname, names, self.yearOfStuding, number)
                self.students.append(s)
    def __isItAModul(self, text):
        x = re.findall("\d\d\d\d\d\d.M\d.[J,P]\d", text)
        if (x != []):
            return True
        else:
            return False

    def __isItARating(self, text):
       if text.find("niedostateczny")>-1:
           return True
       if text.find("nieklasyfikowan")>-1:
           return True
       elif text.find("dopuszczający")>-1:
           return True
       elif text.find("dostateczny") > -1:
           return True
       elif text.find("dobry") > -1:
           return True
       elif text.find("celujący") > -1:
           return True
       else:
           return False
    def __readARating(self,text):
        if text.find("niedostateczny") > -1:
            return 1
        if text.find("nieklasyfikowan") > -1:
            return "nk"
        elif text.find("dopuszczający") > -1:
            return 2
        elif text.find("dostateczny") > -1:
            return 3
        elif text.find("bardzo dobry") > -1:
            return 5
        elif text.find("dobry") > -1:
            return 4
        elif text.find("celujący") > -1:
            return 6
    def readAllDegrees(self):
        for i in range(1,self.yearOfStuding):
            self.makeIntersection(i)
    def makeIntersection(self,year):
        oldGroup=GroupOfStudents(self.prefix,year)
        for s in self.students:
            self.__rewriteDegrees(s,oldGroup)
    def __rewriteDegrees(self,s,oldGroup):
        flag=False
        for os in oldGroup.students:
            if os.names==s.names and os.surname==s.surname:
                for r in os.ratings:
                    s.ratings.append(r)
                flag=True
        if not flag:
            s.state="Brak Ocen z poprzednich lat."
    def calculateDegrees(self):
        for s in self.students:
            s.calculateFinalsRatings(self.net)

    def writeRatingsToTheFile(self):
        f = open(self.prefix+"oceny.txt", "w")
        for s in self.students:
            f.write(s. writeFinalRatings())
