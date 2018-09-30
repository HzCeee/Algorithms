class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        vocab = str.split(" ")
        if len(pattern) != len(vocab):
            return False
        vocabPatternMapping = dict()
        patternVocabMapping = dict()
        for p, v in zip(pattern, vocab):
            if p not in patternVocabMapping:
                patternVocabMapping[p] = v
            if v not in vocabPatternMapping:
                vocabPatternMapping[v] = p
            if patternVocabMapping[p] != v or vocabPatternMapping[v] != p:
                return False
        return True
            
                