class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n, maxLen = len(s), 0
        start, mapping = 0, {}
        
        for i in range(n):
            char = s[i]
            
            if char in mapping:
                start = max(mapping[char], start)
                
            maxLen = max(maxLen, i - start + 1)
            mapping[char] = i + 1
            
        return maxLen