class Solution:
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        from heapq import heappop, heappush
        
        endState = [1, 2, 3, 4, 5, 0]
        possibleSwaps = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4], 4: [1, 3, 5], 5: [2, 4]}
        
        stateQueue = [(0, board[0]+board[1])]
        visitedState = set()
        while stateQueue:
            step, state = heappop(stateQueue)
            
            if state == endState:
                return step
            
            if tuple(state) in visitedState:
                continue
            visitedState.add(tuple(state))
            
            emptyPos = state.index(0)
            for swapPos in possibleSwaps[emptyPos]:
                nextStep = step + 1
                nextState = state.copy()
                nextState[emptyPos], nextState[swapPos] = nextState[swapPos], nextState[emptyPos]
                heappush(stateQueue, (nextStep, nextState))
                
        return -1
            