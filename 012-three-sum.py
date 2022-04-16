class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n, i  = len(nums), 0
        sorted_nums, triplets = sorted(nums), []
        
        for i in range(n - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]: continue

            j, k = i + 1, n - 1
            
            while j < k:
                total = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                if total == 0:
                    triplets.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    while j < k and sorted_nums[j] == sorted_nums[j + 1]:
                        j += 1
                    while j < k and sorted_nums[k] == sorted_nums[k - 1]:
                        k -= 1
                        
                    j += 1
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
                    
            i += 1
                    
        return triplets