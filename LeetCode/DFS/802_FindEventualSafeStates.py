class Solution:
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        outNodes = {}
        for node, outEdge in enumerate(graph):
            outNodes[node] = outEdge
        
        memo = {}
        
        # return bool value if the node is eventually safe
        def eventualSafeNodesHelper(node, visitedNodes):
            if node in memo: return memo[node]
            if node in visitedNodes: return False
            
            visitedNodes.add(node)
            
            if not outNodes[node]:
                memo[node] = True
                return True
            
            for outNode in outNodes[node]:
                if not eventualSafeNodesHelper(outNode, visitedNodes):
                    memo[node] = False
                    return False
            
            memo[node] = True
            return True
        
        ans = sorted([i for i in range(len(graph)) if eventualSafeNodesHelper(i, set())])
        return ans