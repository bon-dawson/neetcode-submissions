class Solution:
    # def solveNQueens(self, n: int) -> List[List[str]]:
    #     res = []
        
    #     def dfs(cur, r, col, pos_diag, neg_diag):
    #         if r == n:
    #             res.append(cur.copy())
    #             return

    #         for c in range(n):
    #             if col[c] or pos_diag[r + c] or neg_diag[r - c]:
    #                 continue
                
    #             col[c] = True
    #             pos_diag[r + c] = True
    #             neg_diag[r - c] = True
    #             cur[r] = cur[r][:c] + 'Q' + cur[r][c + 1:]
    #             dfs(cur, r + 1, col, pos_diag, neg_diag)
    #             cur[r] = cur[r][:c] + '.' + cur[r][c + 1:]
    #             col[c] = False
    #             pos_diag[r + c] = False
    #             neg_diag[r - c] = False


    #     dfs([('.' * n) for _ in range(n)], 0, defaultdict(bool), defaultdict(bool), defaultdict(bool))

    #     return res
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        col = pos_diag = neg_diag = 0

        def backtracking(r):
            nonlocal col, pos_diag, neg_diag
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if ((col & (1 << c)) or (pos_diag & (1 << (r + c))) 
                    or (neg_diag & (1 << (r - c + n)))):
                    continue

                col ^= (1 << c)
                pos_diag ^= (1 << (r + c))
                neg_diag ^= (1 << (r - c + n))
                board[r][c] = "Q"
                backtracking(r + 1)
                board[r][c] = "."
                col ^= (1 << c)
                pos_diag ^= (1 << (r + c))
                neg_diag ^= (1 << (r - c + n))

        backtracking(0)
        return res