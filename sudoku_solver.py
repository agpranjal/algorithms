
class Solution:
    def is_safe(self, board, row, col, value):
    
        if value in board[row]:
            return False
        
        for i in range(len(board)):
            if value == board[i][col]:
                return False
        
        
        sub_grid = [[0,1,2],[3,4,5],[6,7,8]]
        r = row//3
        c = col//3
        
        ROW = sub_grid[r]
        COL = sub_grid[c]
        
        for r in ROW:
            for c in COL:
                if board[r][c] == value:
                    return False
        
        return True
                
    def solve(self, board, row=0, col=0):
        
        if row == len(board):
            return True

        if board[row][col] == 0:
            for x in range(1, 9+1):
                if self.is_safe(board, row, col, x):
                    board[row][col] = x

                    if col+1 == len(board):
                        if self.solve(board, row+1, 0):
                            return True
                    else:
                        if self.solve(board, row, col+1):
                            return True
                        
                    board[row][col] = 0
        else:
            if col+1 == len(board):
                if self.solve(board, row+1, 0):
                    return True
            else:
                if self.solve(board, row, col+1):
                    return True

                  
            
                                    
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        
        self.solve(board)
        return board

board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

obj = Solution()
obj.solveSudoku(board)

for i in range(len(board)):
    print(*board[i])
