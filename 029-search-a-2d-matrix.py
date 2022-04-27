class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nRow, nCol = len(matrix), len(matrix[0])
        
        top, bottom = 0, nRow - 1
        while top <= bottom:
            row = top + (bottom - top) // 2
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bottom = row - 1
            else:
                break
                
        if not (top <= bottom):
            return False
        
        left, right = 0, nCol - 1
        row = top + (bottom - top) // 2
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[row][mid] > target:
                right = mid - 1
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                return True
            
        return False