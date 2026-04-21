class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m = len(board)
        n = len(board[0])

        def dfs(r,c):
            if 0 > r or r >= m or 0 > c or c >= n or board[r][c] != "O":
                return

            board[r][c] = "T"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(m):
            dfs(r,0)
                
            dfs(r,n-1)

        for c in range(n):
            
            dfs(0,c)
            
            dfs(m-1,c)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "T":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X" 

        


            


        