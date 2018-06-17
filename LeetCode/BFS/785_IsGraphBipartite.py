class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        
        subsets = [set(), set()]
        allNodes = set(range(len(graph)))
        visitedNodes = set()
        nodeIndexQueue = []
        
        while len(visitedNodes) != len(graph):
            newNode = list(allNodes.difference(visitedNodes))[0]
            nodeIndexQueue.append((newNode, 0))
            while nodeIndexQueue:
                node, index = nodeIndexQueue.pop(0)

                if node in visitedNodes: continue
                visitedNodes.add(node)
                subsets[index].add(node)

                for adjNode in graph[node]:
                    nodeIndexQueue.append((adjNode, 1-index))
                    if adjNode in subsets[index]:
                        return False

        return True