class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[position[i], (target - position[i]) / speed[i]] for i in range(len(position))]
        pairs.sort()
        
        fleets = []
        
        for i in range(len(pairs) - 1, -1 ,-1):
            if not fleets or fleets[-1][1] < pairs[i][1]:
                fleets.append(pairs[i])
                
        return len(fleets)