class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        counter = {}

        for char in s:
            counter[char] = counter.get(char, 0) + 1

        for char in t:
            counter[char] = counter.get(char, 0) - 1

        for count in counter.values():
            if count != 0:
                return False
        return True