class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # return (BOOL, the list of possible palindrome partitioning of string)
        def partitionHelper(string):
            if string == "":
                return (True, [])
            
            allPalindromes = []
            for i in range(1, len(string) + 1):
                if string[:i] == string[:i][::-1]:
                    isValid, palindromes = partitionHelper(string[i:])
                    if isValid:
                        if not palindromes: 
                            allPalindromes.append([string[:i]])
                        for palindrome in palindromes:
                            allPalindromes.append([string[:i]] + palindrome)
            
            return (True, allPalindromes) if allPalindromes else (False, [])
        
        return partitionHelper(s)[1]
                