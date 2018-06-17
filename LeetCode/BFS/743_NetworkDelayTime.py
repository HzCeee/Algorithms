class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        edgeTime, adjNodes = {}, {}
        for source, target, time in times:
            edgeTime[(source, target)] = time
            if source not in adjNodes:
                adjNodes[source] = [target]
            else:
                adjNodes[source].append(target)
        
        time = {node: float("inf") for node in range(1, N+1)}
        time[K] = 0
        
        visitedNodes = set()
        
        from heapq import heappush, heappop
        nodeQueue = [(time[K], K)]
        
        # print(nodeQueue.queue)
        while nodeQueue:
            curTime, curNode = heappop(nodeQueue)
            if curNode in visitedNodes: continue
            visitedNodes.add(curNode)
            for adjNode in adjNodes.get(curNode, []):
                time[adjNode] = min(time[adjNode], curTime+edgeTime[(curNode, adjNode)])
                heappush(nodeQueue, (time[adjNode], adjNode))
        
        maxTime = max(time.values())
        return maxTime if maxTime < float("inf") else -1