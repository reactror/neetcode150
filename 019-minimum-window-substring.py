class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mapping = Counter()
        start, end, resStart, resLen, counter = 0, 0, 0, float('inf'), len(t)
        
        for char in t:
            mapping[char] += 1
            
        while end < len(s):
            char = s[end]
            if mapping[char] > 0:
                counter -= 1
            mapping[char] -= 1
            end += 1
            
            while counter == 0:
                if end - start < resLen:
                    resLen = end - start
                    resStart = start
                    
                mapping[s[start]] += 1
                if mapping[s[start]] > 0:
                    counter += 1
                    
                start += 1
                
        if resLen != float('inf'):
            return s[resStart: resStart + resLen]
        return ''