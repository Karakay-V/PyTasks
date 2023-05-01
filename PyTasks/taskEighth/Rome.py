class Rome:
    def toRoman(num: int) -> str:

        value = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        sym = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

        index = 0
        result = ""
        
        while num > 0:
            res = num // value[index]
            num = num % value[index]

            while res > 0:
                result = result + sym[index]
                res = res - 1

            index += 1

        return  result