class Trie:
    
    class TrieNode():
        def __init__(self):
            self.val = dict()
            self.isWordEnding = False
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.TrieNode()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curNode = self.root
        for char in word:
            if char not in curNode.val:
                curNode.val[char] = self.TrieNode()
            curNode = curNode.val[char]
        curNode.isWordEnding = True  
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curNode = self.root
        for char in word:
            if char not in curNode.val:
                return False
            curNode = curNode.val[char]
        return False if not curNode.isWordEnding else True
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curNode = self.root
        for char in prefix:
            if char not in curNode.val:
                return False
            curNode = curNode.val[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)