class Solution:
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        # return list of possible next levels
        def possibleNextLevels(level):
            if len(level) == 2:
                return [blockTriple[-1] for blockTriple in allowed if blockTriple[:2] == level]
            
            nextLevels = []
            for firstBlock in possibleNextLevels(level[:2]):
                for remainedBlocks in possibleNextLevels(level[1:]):
                    nextLevels.append(firstBlock + remainedBlocks)
                    
            return nextLevels
        
        # return True if we can stack the pyramid to the top.
        def pyramidTransitionHelper(level):
            if len(level) == 1: return True
            
            for nextLevel in possibleNextLevels(level):
                if pyramidTransitionHelper(nextLevel): return True
            
            return False
        
        return pyramidTransitionHelper(bottom)