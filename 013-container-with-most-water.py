class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxAmount, l, r = 0, 0, len(height) - 1
        
        while l < r:
            maxAmount = max(maxAmount, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return maxAmount