# 1
from PyTasks.taskFirst import taskFirst
# 2
from PyTasks.taskSecond import taskSecond
# 3
from PyTasks.taskThird import taskThird
# 4
from PyTasks.taskFourth import taskFourth
# 5
from PyTasks.taskFifth import taskFifth
# 6
from PyTasks.taskSixth import taskSixth
# 7
from PyTasks.taskSeventh.Person import Person
from PyTasks.taskSeventh.modifier import modifier
# 8
from PyTasks.taskEighth.Rome import Rome
from PyTasks.taskEighth.Decimal import Decimal

'''---------RUN----------'''

# taskFirst()
# taskSecond()
# taskThird()
# taskFourth()
# taskFifth()
# taskSixth()

Linus = modifier("persons.csv", 2)

print(Linus.firstname)
print(Linus.surname)
print(Linus.nickname)
print(Linus.birthday)
print(Linus.getFullname(Linus))
print(Linus.getAge(Linus))

# rome = Rome
# decimal = Decimal

'''---------RUN----------'''
