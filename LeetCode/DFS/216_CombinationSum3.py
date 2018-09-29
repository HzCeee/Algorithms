class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        output = []
        # find all combinations
        def combinationSum3Helper(seen, count, target):
            # base case
            if count == 1:
                if target > seen[-1] and 1 <= target <= 9:
                    output.append(seen + [target])
                return
            
            # keep seen in increasing order
            minNumber = 1 if not seen else seen[-1] + 1
            for num in range(minNumber, (target+1)//count):
                combinationSum3Helper(seen+[num], count-1, target-num)
        
        combinationSum3Helper([], k, n)
        
        return output
    