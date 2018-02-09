class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = {course: [] for course in range(numCourses)}
        preqNode = {course: [] for course in range(numCourses)}
        ordering = []
        
        for course, preqCourse in prerequisites:
            if preqCourse not in graph[course]:
                graph[course].append(preqCourse)
                preqNode[course].append(preqCourse)
            
        nodeStack = [node for node in preqNode if not preqNode[node]]
        
        while nodeStack:
            curNode = nodeStack.pop()
            ordering.append(curNode)
            
            for node in preqNode:
                if curNode in preqNode[node]:
                    preqNode[node].remove(curNode)
                    if not preqNode[node]: 
                        nodeStack.append(node)
            
            graph.pop(curNode)
        
        print(graph)
        
        return ordering if not graph else []