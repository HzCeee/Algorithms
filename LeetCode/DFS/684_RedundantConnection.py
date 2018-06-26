class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # construct adjacency list
        neighborNodes = {}
        for u, v in edges:
            if u not in neighborNodes:
                neighborNodes[u] = []
            if v not in neighborNodes:
                neighborNodes[v] = []
            neighborNodes[u].append(v)
            neighborNodes[v].append(u)
        
        # find circle
        visitingNodes = set()
        parentNodes = {}
        entryNodeGlobal = [None]
        
        def traversal(parentNode, node):
            if node in visitingNodes: 
                entryNodeGlobal[0] = node
                parentNodes[node] = parentNode
                return
            visitingNodes.add(node)
            
            parentNodes[node] = parentNode
            
            for adjNode in neighborNodes[node]:
                if adjNode != parentNode:
                    traversal(node, adjNode)
                
            visitingNodes.remove(node)
        
        traversal(None, 1)
        
        # contruct circle
        entryNode = entryNodeGlobal[0]
        circle = [sorted([parentNodes[entryNode], entryNode])]
        curNode = parentNodes[entryNode]
        while curNode != entryNode:
            curParentNode = parentNodes[curNode]
            circle.append(sorted([curParentNode, curNode]))
            curNode = curParentNode
        
        for edge in edges[::-1]:
            if edge in circle: return edge
            