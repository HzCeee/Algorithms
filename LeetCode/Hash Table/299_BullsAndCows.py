class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bullCount, cowCount = 0, 0
        digitCountDict = dict()
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bullCount += 1
                continue
            if secret[i] not in digitCountDict:
                digitCountDict[secret[i]] = 0
            digitCountDict[secret[i]] += 1
            
        for i in range(len(guess)):
            if secret[i] != guess[i]:
                if guess[i] in digitCountDict and digitCountDict[guess[i]] > 0:
                    digitCountDict[guess[i]] -= 1
                    cowCount += 1
                    
        return str(bullCount) + "A" + str(cowCount) + "B"                    