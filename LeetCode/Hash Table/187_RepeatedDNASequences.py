class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = set()
        repeatedSequences = set()
        for i in range(len(s) - 9):
            substr = s[i: i+10]
            if substr not in seen:
                seen.add(substr)
            else:
                repeatedSequences.add(substr)
        
        return list(repeatedSequences)