class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numIndice = dict()
        for index, num in enumerate(nums):
            if num not in numIndice:
                numIndice[num] = []
            numIndice[num].append(index)
        for indice in numIndice.values():
            for i in range(len(indice) - 1):
                if indice[i+1] - indice[i] <= k:
                    return True
        return False