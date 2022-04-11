class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lProd, rProd = [1] * n, [1] * n
        
        for i in range(1, n):
            lProd[i] = lProd[i - 1] * nums[i - 1]
            
        for i in range(n - 2, -1, -1):
            rProd[i] = rProd[i + 1] * nums[i + 1]
            
        ans = []
        for i in range(n):
            ans.append(lProd[i] * rProd[i])
            
        return ans

        # O(n)