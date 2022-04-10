class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = collections.defaultdict(list)
        
        for s in strs:
            counter = [0] * 26
            for char in s:
                counter[ord(char) - ord('a')] += 1
            group[tuple(counter)].append(s)
            
        return group.values()