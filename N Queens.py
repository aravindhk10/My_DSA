class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = ["."*n for _ in range(n)]
        left = [0]*n
        dwn_left = [0]*((2*n)-1)
        up_left = [0]*((2*n)-1)
        def solve(col, ans, board, left, dwn_left, up_left, n):
            if (col == n) :
                ans.append(board[:])
                return
            for i in range(n):
                if (left[i] == 0 and up_left[(n-1)+(col-i)] == 0 and dwn_left[i + col] == 0):
                    board[i] = board[i][:col] + "Q" + board[i][(col+1):]
                    left[i] = 1
                    dwn_left[i + col] = 1
                    up_left[(n-1)+(col-i)] = 1
                    solve(col+1, ans, board, left, dwn_left, up_left, n)
                    board[i] = board[i][:col] + "." + board[i][(col+1):]
                    left[i] = 0
                    dwn_left[i + col] = 0
                    up_left[(n-1)+(col-i)] = 0
            return ans
        return solve(0, ans, board, left, dwn_left, up_left, n)
