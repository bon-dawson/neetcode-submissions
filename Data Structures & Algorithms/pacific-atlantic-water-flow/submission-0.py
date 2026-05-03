class Solution:
    def pacificAtlantic(self, height: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(height), len(height[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prev_height):
            if (r,c) in visit or r < 0 or r == ROWS or c < 0 or c == COLS or height[r][c] < prev_height:
                return

            visit.add((r, c))

            dfs(r + 1, c, visit, height[r][c])
            dfs(r, c + 1, visit, height[r][c])
            dfs(r - 1, c, visit, height[r][c])
            dfs(r, c - 1, visit, height[r][c])

        for c in range(COLS):
            dfs(0, c, pac, height[0][c])
            dfs(ROWS -1 , c, atl, height[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, height[r][0])
            dfs(r, COLS - 1, atl, height[r][COLS - 1])

        ans = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    ans.append([r,c])
        
        return ans