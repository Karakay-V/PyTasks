import datetime
date = datetime.date
today = datetime.datetime.today()

class Person:
    firstname = "Vlad"
    surname = "Karakay"
    nickname = "karakenza"
    birthday = date(2005, 6, 2)
    def getAge(self):
        current = today.year
        age = current - self.birthday.year
        return age
    def getFullname(self):
        fullname = self.surname +" "+ self.firstname
        return fullname