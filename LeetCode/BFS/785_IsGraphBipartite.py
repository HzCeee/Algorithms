class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        
        subsets = [set(), set()]
        allNodes = set(range(len(graph)))
        visitedNodes = set()
        nodeIndexQueue, nodeQueue = [], set()
        
        while len(visitedNodes) != len(graph):
            newNode = list(allNodes.difference(visitedNodes))[0]
            nodeIndexQueue.append((newNode, 0))
            nodeQueue.add(newNode)
            while nodeIndexQueue:
                node, index = nodeIndexQueue.pop(0)

                visitedNodes.add(node)
                subsets[index].add(node)

                for adjNode in graph[node]:
                    if adjNode not in visitedNodes and adjNode not in nodeQueue:
                        nodeIndexQueue.append((adjNode, 1-index))
                        nodeQueue.add(adjNode)
                    if adjNode in subsets[index]:
                        return False

        return True
            
                
            