import random

def taskSixth():
    students =  [
        "Vlad Karakay",
        "Oleksa Biloschura",
        "Taras Grigorovich",
        "Mamaeb Oleksandr"
    ]
    # data = ["number,student,grade"]
    marks = open("marks.csv", "+a")
    for i in students:
        student = str(i)+","+students[i]+","+str(random.randint(0,5))
        print(student)
        # data.append(student)
    # print(data)