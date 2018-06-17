class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def generateNeighborWords(word, wordList):
            import string
            neighborWords = []
            for index in range(len(word)):
                for char in string.ascii_lowercase:
                    possibleWord = word[:index] + char + word[index+1:]
                    if possibleWord in wordList:
                        yield possibleWord
            # return neighborWords
        
        if endWord not in wordList: return 0
        
        wordList = set(wordList)
        
        from collections import deque
        wordQueue = deque([(beginWord, 0)])
        
        triedWords = set()
        while wordQueue:
            word, step = wordQueue.popleft()
            
            if word == endWord: return step + 1
            
            if word in triedWords: continue
            triedWords.add(word)
            
            for nextWord in generateNeighborWords(word, wordList):
                wordQueue.append((nextWord, step+1))
        
        return 0