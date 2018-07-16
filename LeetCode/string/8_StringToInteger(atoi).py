class Solution:
    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        maxInt, minInt = 2**31 - 1, -2**31
        
        while string and string[0] == " ":
            string = string[1:]
        
        if not string or string[0].isalpha() or (not string[0].isdigit() and string[0] not in ["-", "+"]): return 0
        
        res = ""
        if not string[0].isdigit():
            res = "-" if string[0] == "-" else ""
            string = string[1:]
            
        numExists = False
        while string and string[0].isdigit():
            numExists = True
            res += string[0]
            string = string[1:]
        
        res = min(max(int(res), minInt), maxInt) if numExists else 0
        
        return res
        