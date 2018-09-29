class WordDictionary:
    class dictNode():
        def __init__(self):
            self.val = dict()
            self.isWordEndding = False
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.dictNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curNode = self.root
        for char in word:
            if char not in curNode.val:
                curNode.val[char] = self.dictNode()
            curNode = curNode.val[char]
        curNode.isWordEndding = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        curNode = self.root
        for index, char in enumerate(word):
            if char == ".":
                for c in curNode.val:
                    newWord = word[:index] + c + word[index+1:]
                    if self.search(newWord):
                        return True
                return False
            else:
                if char not in curNode.val:
                    return False
                curNode = curNode.val[char]
        return True if curNode.isWordEndding else False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)