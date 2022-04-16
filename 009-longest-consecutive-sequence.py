class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)

        longestSeq = 0

        for num in nums:
            if num - 1 not in numsSet:
                curSeq, cur = 1, num
                while cur + 1 in numsSet:
                    curSeq += 1
                    cur += 1

                longestSeq = max(longestSeq, curSeq)

        return longestSeq