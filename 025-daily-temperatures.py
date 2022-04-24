class Solution:
    def dailyTemperaturesForward(self, temperatures: List[int]) -> List[int]:
        stack, res = [], [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
            
        return res
            
    def dailyTemperatureBackward(self, temperatures: List[int]) -> List[int]:
        stack, res = [], [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]: stack. pop()
            res[i] = 0 if not stack else stack[-1] - i
            stack.append(i)

        return res