class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        for word in sorted(d, key = lambda w: (-len(w), w)):
            iterS = iter(s)
            if all(char in iterS for char in word):
                return word
        return ''