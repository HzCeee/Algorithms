class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        # for word in sorted(d, key = lambda w: (-len(w), w)):
        #     iterS = iter(s)
        #     if all(char in iterS for char in word):
        #         return word
        # return ''
    
        # index denotes the index of the start element in search s
        
        sortedD = sorted(d, key = lambda word: (-len(word), word))
        for word in sortedD:
            index = 0
            isMatch = True
            for char in word:
                while index < len(s) and s[index] != char:
                    index += 1
                if index < len(s):
                    index += 1
                else:
                    isMatch = False
                    break
            if isMatch: return word
        
        return ''