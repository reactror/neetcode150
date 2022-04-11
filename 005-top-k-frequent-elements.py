class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        frequencies = [[] for i in range(len(nums) + 1)]

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for num, count in counter.items():
            frequencies[count].append(num)

        ans = []
        for i in range(len(frequencies) - 1, 0, -1):
            for num in frequencies[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans

        # O(n)
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from heapq import heapify, heappop
        from collections import Counter
        res = []
        counter = Counter(nums)
        heap = [(-val, key) for key, val in counter.items()]
        heapify(heap)
        
        for _ in range(k):
            res.append(heappop(heap)[1])
            
        return res

        # O(nlogk)