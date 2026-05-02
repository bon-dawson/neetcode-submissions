class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        
        def dfs(cur, r, col, pos_diag, neg_diag):
            if r == n:
                res.append(cur.copy())
                return

            for c in range(n):
                if col[c] or pos_diag[r + c] or neg_diag[r - c]:
                    continue
                
                col[c] = True
                pos_diag[r + c] = True
                neg_diag[r - c] = True
                cur[r] = cur[r][:c] + 'Q' + cur[r][c + 1:]
                dfs(cur, r + 1, col, pos_diag, neg_diag)
                cur[r] = cur[r][:c] + '.' + cur[r][c + 1:]
                col[c] = False
                pos_diag[r + c] = False
                neg_diag[r - c] = False


        dfs([('.' * n) for _ in range(n)], 0, defaultdict(bool), defaultdict(bool), defaultdict(bool))

        return res