class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        rows = len(board)
        cols = len(board[0])
        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            if board[row][col] != "O":
                return
            board[row][col] = "S"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        for i in range(rows):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][cols - 1] == "O":
                dfs(i, cols - 1)
        for j in range(cols):
            if board[0][j] == "O":
                dfs(0, j)
            if board[rows - 1][j] == "O":
                dfs(rows - 1, j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"