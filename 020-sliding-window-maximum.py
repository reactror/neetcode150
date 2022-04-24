class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        
        maxWindow = []
        for i, n in enumerate(nums):
            while queue and n > queue[-1][1]:
                queue.pop()
                
            queue.append((i, n))
            
            while i - queue[0][0] + 1 > k:
                queue.popleft()
            if i + 1 >= k:
                maxWindow.append(queue[0][1])
                
        return maxWindow