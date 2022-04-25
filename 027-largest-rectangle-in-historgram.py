class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, maxArea, n = [], 0, len(heights)
        
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                left = stack[-1] + 1 if stack else 0
                maxArea = max(maxArea, height * (i - left))
                
            stack.append(i)
            
        while stack:
            height = heights[stack.pop()]
            left = stack[-1] + 1 if stack else 0
            maxArea = max(maxArea, height * (n - left))
            
        return maxArea