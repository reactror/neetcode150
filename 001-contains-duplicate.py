class Solution:
    def containsDuplicate1(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

    def containsDuplicate2(self, nums: List[int]) -> bool:
        hashset = set()

        for num in nums:
            if num in hashset:
                return True

            hashset.add(num)

        return False