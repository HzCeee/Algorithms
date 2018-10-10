class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        relationDatabase = dict()
        for equation, value in zip(equations, values):
            a, b = equation
            if a not in relationDatabase:
                relationDatabase[a] = dict()
            relationDatabase[a][b] = value
            if b not in relationDatabase:
                relationDatabase[b] = dict()
            relationDatabase[b][a] = 1 / value
        
        def calcEquationHelper(curNode, target, prevValue, visitedNode):
            if curNode not in relationDatabase:
                return -1.0
            
            if target in relationDatabase[curNode]:
                return prevValue * relationDatabase[curNode][target]
            
            for nextNode in relationDatabase[curNode]:
                if nextNode in visitedNode:
                    continue
                visitedNode.add(nextNode)
                curValue = relationDatabase[curNode][nextNode]
                ans = calcEquationHelper(nextNode, target, prevValue*curValue, visitedNode)
                if ans != -1.0:
                    return ans
                
            return -1.0
        
        res = []
        for query in queries:
            nominator, denominator = query
            res.append(calcEquationHelper(nominator, denominator, 1.0, set([nominator])))
        
        return res
            
            
            