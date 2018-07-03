class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        minDiff, minElem = float("inf"), None
        for letter in letters:
            ordDiff = ord(letter) - ord(target)
            diff = ordDiff if ordDiff > 0 else 26 + ordDiff
            if minDiff > diff:
                minDiff = diff
                minElem = letter
        return minElem