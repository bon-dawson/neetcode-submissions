class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != '1':
                return

            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)
        
        ans = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1

        return ans