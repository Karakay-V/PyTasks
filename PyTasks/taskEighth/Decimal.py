class Decimal:
    def toDecimal(str: str) -> int:
        
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }    
        num = 0

        for i in range(len(str)-1):

            if roman[str[i]] < roman[str[i+1]]:
                num += roman[str[i]]*-1
                continue

            num += roman[str[i]]
        num +=roman[str[-1]]
        return  num