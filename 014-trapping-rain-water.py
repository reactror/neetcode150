class Solution:
    def trapTwoPointers(self, height: List[int]) -> int:
        if not len(height): return 0

        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        water = 0
        
        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                water += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                water += maxR - height[r]
                
        return water

    def trapStack(self, height: List[int]) -> int:
        stack, total, right = [], 0, 0

        while right < len(height):
            while stack and height[stack[-1]] < height[right]:
                bottom = stack.pop()

                if not stack:
                    break

                dist = right - stack[-1] - 1
                bounded_height = min(stack[-1], stack[right]) - height[bottom]
                total += dist * bounded_height

            stack.append(right)
            right += 1

        return total
                