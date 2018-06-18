class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def findCircleNumHelper(node):
            visitedNodes.add(node)
            for neighborNode in range(len(M)):
                if M[node][neighborNode] == 1:
                    if neighborNode in visitedNodes: continue
                    findCircleNumHelper(neighborNode)
            return 1
        
        circleNumber = 0
        visitedNodes = set()
        
        for node in range(len(M)):
            if node in visitedNodes: continue
            circleNumber += findCircleNumHelper(node)
        
        return circleNumber
        
        
            