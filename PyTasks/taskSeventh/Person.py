import datetime
date = datetime.date
today = datetime.datetime.today()

class Person:
    firstname = "Vlad"
    surname = "Karakay"
    nickname = "karakenza"
    birthday = date(2005, 6, 2)
    def getAge():
        current = today.year
        age = current - Person.birthday.year
        return age
    def getFullname():
        fullname = Person.surname +" "+ Person.firstname
        return fullname