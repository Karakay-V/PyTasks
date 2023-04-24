import string

# 7
def taskThird():

    # ОГОЛОШЕННЯ СТРОКИ З РАНДОМНИМИ ЗНАЧЕННЯМИ
    randomString = string.printable

    # ОГОЛОШЕННЯ ПОЛОВИНИ ДОВЖИНИ ВІД СТРОКИ
    randomStringlength = len(randomString)/2

    print(
        "\n"+"\\---------------------ЛАБОРАТОРНА РОБОТА №3---------------------//\n"
    )
    print("\\---------------------ВИВІД---------------------//\n")

    # ВИКЛИК ЦИКЛУ З ПЕРЕБОРОМ СТРОКИ
    for i in range(len(randomString)):

        # БЕРЕМО ЗНАЧЕННЯ і-ТОГО СИМВОЛУ З СТРОКИ
        index = randomString[i]

        # ЯКЩО і МЕНЬШЕ РІВНО ПОЛОВИНІ СТРОКИ
        if i <= randomStringlength:
            # ВИВОДИМО "*"
            print(str(randomString[i].replace(index, "*")))
        # ІНАКШЕ
        else:
            # ВИВОДИМО ПОЧАТКОВИЙ ЕЛЕМЕНТ СТРОКИ
            print(str(randomString[i]))

    print(
        "\n"+"\\---------------------ВИСНОВКИ---------------------//\n"+
        "\nПід час виконання цієї лабораторної роботи я застосував нову для встроєну бібліотеку string для взяття рандомних символів."
    )

    return randomString

    # І ЗНОВУ ПОМИЛКОВО ПОЧАВ РОБИТИ ІНШЕ ЗАВДАННЯ...
    # ВИДАЛЯТИ ШКОДА(

    '''
    def square_root(numbers):

        result = []
        n = len(numbers)
        for i, number in enumerate(numbers):
            print(f"Processing number: {number}")
            result.append(math.sqrt(number))
            print(f"Completed: {int((i + 1) / n * 100)}%")
        return result

    numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81]
    square_root(numbers)
    '''
