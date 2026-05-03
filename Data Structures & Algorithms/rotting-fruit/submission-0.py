class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        ans = 0
        while fresh > 0 and q:
            n = len(q)
            for _ in range(n):
                r, c = q.popleft()

                for dx, dy in directions:
                    nr, nc = r + dx, c + dy

                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] != 1:
                        continue

                    fresh -= 1
                    grid[nr][nc] = 0
                    q.append((nr, nc))
            ans += 1

        return ans if fresh == 0 else -1