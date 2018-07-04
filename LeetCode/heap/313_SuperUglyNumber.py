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
    
        nextMultiplyPrimeIndex = [0 for _ in range(len(primes))]
        uglyNumbers = [1]
        heap = [(prime, originalIndex) for originalIndex, prime in enumerate(primes)]
        while len(uglyNumbers) < n:
            prime, originalIndex = heapq.heappop(heap)
            nextMultiplyPrimeIndex[originalIndex] += 1
            if prime > uglyNumbers[-1]:
                uglyNumbers.append(prime)
            heapq.heappush(heap, (primes[originalIndex] * uglyNumbers[nextMultiplyPrimeIndex[originalIndex]], originalIndex))
        return uglyNumbers[n-1]
        