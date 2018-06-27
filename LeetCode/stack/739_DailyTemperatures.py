class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)

        return ans