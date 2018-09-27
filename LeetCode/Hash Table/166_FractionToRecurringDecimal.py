class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        isNegative = True if numerator * denominator < 0 else False
        print(isNegative)
        numerator, denominator = abs(numerator), abs(denominator)
        
        quotient = numerator // denominator
        remainder = numerator - numerator // denominator * denominator
        resStr = str(quotient)
        if remainder == 0: 
            return ("-" if isNegative else "") + resStr
        else:
            resStr += "."
        
        numeratorIndex = dict()
        indexCount = 0
        while True:
            numerator = remainder * 10
            if numerator in numeratorIndex:
                break
            numeratorIndex[numerator] = indexCount
                
            quotient = numerator // denominator
            remainder = numerator - numerator // denominator * denominator
            resStr += str(quotient)
            
            if remainder == 0: 
                return ("-" if isNegative else "") + resStr
            
            indexCount += 1
            
        ptIndex = resStr.index(".")
        startPtr, endPtr = ptIndex + numeratorIndex[numerator] + 1, ptIndex + indexCount + 1
        resStr = resStr[:startPtr] + "(" + resStr[startPtr: endPtr] + ")"
        
        return ("-" if isNegative else "") + resStr