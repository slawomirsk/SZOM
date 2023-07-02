from groupOfStudents import GroupOfStudents
if __name__ == '__main__':
    prefix="klasy/dobre/3ti1/"
    mineGroupOfStudents=GroupOfStudents(prefix,3)

    mineGroupOfStudents.readAllDegrees()
    mineGroupOfStudents.calculateDegrees()
    mineGroupOfStudents.writeRatingsToTheFile()

    for s in mineGroupOfStudents.students:
        s.printDate()
        s.printFinalRatings()




