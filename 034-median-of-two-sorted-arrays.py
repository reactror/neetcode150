class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        halfLen = (m + n) // 2
        
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
            
        l, r = 0, m - 1
        while True:
            i = l + (r - l) // 2
            j = halfLen - i - 2
            
            oneLeft = nums1[i] if i >= 0 else float('-infinity')
            oneRight = nums1[i + 1] if (i + 1) < m else float('infinity')
            twoLeft = nums2[j] if j >= 0 else float('-infinity')
            twoRight = nums2[j + 1] if (j + 1) < n else float('infinity')
            
            if oneLeft <= twoRight and twoLeft <= oneRight:
                if (m + n) % 2:
                    return min(oneRight, twoRight)
                return (min(oneRight, twoRight) + max(oneLeft, twoLeft)) / 2
            elif oneLeft > twoRight:
                r = i - 1
            else:
                l = i + 1