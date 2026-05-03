class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = (1 << 31) - 1
        ROWS, COLS = len(grid), len(grid[0])

        q = deque([(r, c) for r in range(ROWS) for c in range(COLS) if grid[r][c] == 0])

        distance = 1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while q:
            n = len(q)
            for i in range(n):
                r, c = q.popleft()

                for dx, dy in directions:
                    nr, nc = r + dx, c + dy

                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] != INF:
                        continue

                    grid[nr][nc] = distance
                    q.append((nr,nc))

            distance += 1