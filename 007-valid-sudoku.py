class Solution:
    def isValidSudokuConcise(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                    
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
                
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nR, nC = len(board), len(board[0])
        for r in range(nR):
            if not self.isValidRow(board, r):
                return False
        
        for c in range(nC):
            if not self.isValidCol(board, c):
                return False
            
        for r in range(0, nR, 3):
            for c in range(0, nC, 3):
                if not self.isValidSquare(board, r, c):
                    return False
                
        return True
            
    
    def isValidSquare(self, board: List[List[str]], row: int, col: int) -> bool:
        seen = set()
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                if board[r][c] in seen:
                    return False
                if board[r][c] != ".":
                    seen.add(board[r][c])
        return True
    
    def isValidRow(self, board: List[List[str]], row: int) -> bool:
        seen = set()
        for cell in board[row]:
            if cell in seen:
                return False
            if cell != ".":
                seen.add(cell)
            
        return True
        
    def isValidCol(self, board: List[List[str]], col: int) -> bool:
        seen = set()
        for r in range(len(board)):
            if board[r][col] in seen:
                return False
            if board[r][col] != ".":
                seen.add(board[r][col])
                
        return True
            