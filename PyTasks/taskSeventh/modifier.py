from PyTasks.taskSeventh.Person import Person
import datetime
date = datetime.date
import csv

def modifier(filename, i):
	person = Person
	with open(filename, "r",) as csvfile:
		csvreader = csv.DictReader(csvfile)
		if (i > 0):
			j = 0
			for row in csvreader:
				j += 1
				if (j == i):
					person.firstname = row['first_name']
					person.surname = row['surname']
					person.nickname = row['nickname']
					person.birthday = date(int(row['birth_year']), int(row['birth_month']), int(row['birth_day']))
		else:
			for i in range(100):
				print("I n c o r r e c t   v a l u e !")
	return person