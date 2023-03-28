import math
import string

# 7
def taskThird():

    randomString = string.printable
    randomStringlength = len(randomString)/2

    for i in range(1):
        for j in range(len(randomString)):
            index = randomString[j]
            if j <= randomStringlength:
                print(str(randomString[j].replace(index, "*")))
            else:
                print(str(randomString[j]))

    return randomString

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
