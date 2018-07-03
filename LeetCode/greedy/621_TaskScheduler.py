class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = collections.Counter(tasks)
        max_cpu = max(count.values())
        
        ans = (max_cpu - 1)*(n + 1) 
        
        for name, cpu in count.items():
            if cpu == max_cpu: ans += 1
                
        return max(len(tasks), ans)