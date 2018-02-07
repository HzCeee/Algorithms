class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # if a node is unvisited, mark it as 0
        # if a node is being visited, mark it as -1
        # if a node has been visited, mark it as 1
        graph = [[] for node in range(numCourses)]
        for course, preCourse in prerequisites:
            graph[course].append(preCourse)
        
        nodeState = [0 for node in range(numCourses)]
        
        def canFinishHelper(node):
            if nodeState[node] == -1:
                return False
            if nodeState[node] == 1:
                return True
            nodeState[node] = -1
            for parentNode in graph[node]:
                if not canFinishHelper(parentNode):
                    return False
            nodeState[node] = 1
            return True
        
        return all(canFinishHelper(course) for course in range(numCourses))
            