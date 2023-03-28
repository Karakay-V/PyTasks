import random
import math

def taskSecond():
    '''Завдання 1'''

    # ОГОЛОШЕННЯ МАССИВУ З МІСЯЦЯМИ
    months = ["January",
              "February",
              "March",
              "April",
              "May",
              "June",
              "July",
              "August",
              "September",
              "October",
              "November",
              "December",
             ]


    # ВИВІД НАЗВ МІСЯЦІВ
    print("\n \\---------------------МІСЯЦІ---------------------//")

    for i in months:
        print(" " + str(i))

    '''Завдання 2'''

    # ФУНКЦІЯ ЩО ДОДАЄ РАНДОМНІ ЧИСЛА В МАССИВ
    def arrayAppendRandomNumbers(array, qua):
        for i in range(qua):
            array.append(random.randint(-10, 10))
        return array

    # ФУНКЦІЯ ЩО ШУКАЄ КІЛЬКІСТЬ ПОЗИТИВНИХ ЧИСЕЛ У МАССИВІ
    def detectPositive(array):
        j = 0
        for number in array:
            if number > 0:
                j + 1
        print("Кількість позитивних чисел: " + str(j))
        return j

    # ВИКЛИК ОБОХ ФУНКЦІЙ
    print("\n \\---------------------ПОЗИТИВНІ-ЗНАЧЕННЯ---------------------//")

    randomNumbers = []
    arrayAppendRandomNumbers(randomNumbers, 3)
    detectPositive(randomNumbers)

    '''Завдання 3'''

    '''
    varOne = random.randint(-10, 10)
    varTwo = random.randint(-10, 10)
    arrayNumbers = []
    
    def betweenSmallAndLarg(array, varOne, varTwo):
        if varOne > varTwo:
            for i in range():
                print()
        elif varOne < varTwo:
            for j in range():
                print()
        else:
            print("Значення рівні")
        return array
    
    print(
          arrayNumbers + 
          varOne
         )
    '''

    '''Завдання 7'''

    varOne = 50
    varTwo = int(input("\nВведіть значення від 0 до 50: "))
    sumVar = 0
    index = varTwo

    for index in range(varOne - varTwo):
        index += 1
        if index < 50:
            mul = index ** 2
            sumVar += mul
        else:
            break

    print(sumVar)

    return "end"