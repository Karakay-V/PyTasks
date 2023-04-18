import random

def taskFifth():
    n = random.randint(10, 100)
    
    def chouseOutput():
        print("Списком : list \nРядками в стовпчик : strg \nКількість символів : leng")
        outputFormat = input(
            "\nЯким чином вивести результат : "
        )

        if(outputFormat == "list" or outputFormat == "LIST"):
            outputList = []
            for i in range(n):
                outputList.append(i)
            print(outputList)
            chouseOutput()

        elif(outputFormat == "strg" or outputFormat == "STRG"):
            outputListStrg = []
            outputStrg = ""
            for j in range(n):
                outputListStrg.append(j)
                outputStrg = outputStrg + " " + str(j)
            print(outputStrg)
            chouseOutput()

        elif(outputFormat == "leng" or outputFormat == "LENG"):
            outputLeng = []
            for i in range(n):
                outputLeng.append(i)
            print(len(outputLeng))
            chouseOutput()

        else:
            print("\nВИБЕРІТЬ ФУНКЦІЮ ІЗ ЗАПРОПОНОВАНИХ!\n")
            chouseOutput()

    chouseOutput()