import datetime
date = datetime.date
today = datetime.datetime.today()

class Person:
    def __init__(self):
        self.firstname = None
        self.firstname = None
        self.surname = None
        self.nickname = None
        self.birthday = None
    def getAge(self):
        current = today.year
        age = current - self.birthday.year
        return age
    def getFullname(self):
        fullname = self.surname +" "+ self.firstname
        return fullname

# firstname = "Vlad"
# surname = "Karakay"
# nickname = "karakenza"
# birthday = date(2005, 6, 2)