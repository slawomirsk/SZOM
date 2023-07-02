class Rating:
    def __init__(self,modul,yearOfStuding,value):
        self.modul=modul
        self.yearOfStuding=yearOfStuding
        self.value=value

class UnitsRating(Rating):
    def __init__(self,modul,unit,yearOfStuding,value):
        super().__init__(modul,yearOfStuding,value)
        self.unit=unit
