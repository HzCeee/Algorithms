class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
#         if primes[0] != 1:
#             primes = [1] + primes
        
#         import heapq
#         heapq.heapify(primes)
        
#         sortedUglyNumbers = []
#         numberAppeared = set(primes)
#         for i in range(n):
#             for numIndex in range(1, i + 1):
#                 candidate = sortedUglyNumbers[numIndex] * sortedUglyNumbers[i]
#                 if candidate not in numberAppeared:
#                     heapq.heappush(primes, candidate)
#                     numberAppeared.add(candidate)
#             sortedUglyNumbers = heapq.nsmallest(i+2, primes)
            
#         # print(sortedUglyNumbers)
#         return sortedUglyNumbers[n - 1]
        
        prime_idx = [0 for _ in xrange(len(primes))]
        uglies = [1]
        heap = [(p, i) for i, p in enumerate(primes)]
        while len(uglies) < n:
            smallest_val, i = heapq.heappop(heap)
            prime_idx[i] += 1
            if smallest_val > uglies[-1]:
                uglies.append(smallest_val)
            heapq.heappush(heap, (primes[i]*uglies[prime_idx[i]], i))
        return uglies[n-1]
        