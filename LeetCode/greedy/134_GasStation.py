class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        tank, need = 0, 0
        startPosIndex = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0: # can't reach station[i+1]
                startPosIndex = i + 1 # any station within [start, i] cant reach (i+1)-th station
                need += tank
                tank = 0
        return -1 if tank + need < 0 else startPosIndex
                