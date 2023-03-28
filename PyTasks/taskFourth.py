import random
import math

def taskFourth():

    randomNumberArray = []

    def appendingFunc(array):
        for i in range(30):
            array.append(random.randint(-100, 100))
            print(array[i])

    appendingFunc(randomNumberArray)

    def bubbleSort(array):
        swapped = False
        n = len(array)

        for i in range(n-1):

            for j in range(0, n-i-1):

                if array[j] > array[j + 1]:
                    swapped = True
                    array[j], array[j + 1] = array[j + 1], array[j]
            if not swapped:
                return

    bubbleSort(randomNumberArray)
    for k in range(len(randomNumberArray)):
        print(randomNumberArray[k])

    return randomNumberArray