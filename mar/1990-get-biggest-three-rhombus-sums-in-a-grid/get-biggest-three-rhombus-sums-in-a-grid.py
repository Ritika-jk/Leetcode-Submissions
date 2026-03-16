class Solution:
    def getBiggestThree(self, grid):
        m, n = len(grid), len(grid[0])

        # Prefix sums along ↘ diagonal and ↙ anti-diagonal
        dp = [[0]*n for _ in range(m)]  # diagonal ↘
        da = [[0]*n for _ in range(m)]  # anti-diagonal ↙

        for i in range(m):
            for j in range(n):
                dp[i][j] = grid[i][j] + (dp[i-1][j-1] if i>0 and j>0 else 0)
                da[i][j] = grid[i][j] + (da[i-1][j+1] if i>0 and j<n-1 else 0)

        def diag(r1, c1, r2, c2):   # ↘ range sum
            res = dp[r2][c2]
            if r1>0 and c1>0: res -= dp[r1-1][c1-1]
            return res

        def anti(r1, c1, r2, c2):   # ↙ range sum
            res = da[r2][c2]
            if r1>0 and c1<n-1: res -= da[r1-1][c1+1]
            return res

        res = set()

        def add_top3(val):
            res.add(val)
            if len(res) > 3:
                res.discard(min(res))

        for r in range(m):
            for c in range(n):
                add_top3(grid[r][c])  # size-0 rhombus
                for k in range(1, min(m, n)):
                    if r-k<0 or r+k>=m or c-k<0 or c+k>=n:
                        break
                    s = (diag(r-k, c,   r,   c+k) +   # top-right edge
                         diag(r,   c-k, r+k, c  ) +   # bottom-left edge
                         anti(r-k, c,   r,   c-k) +   # top-left edge
                         anti(r,   c+k, r+k, c  ) -   # bottom-right edge
                         grid[r-k][c] - grid[r][c+k]  # subtract 4 corners
                       - grid[r+k][c] - grid[r][c-k]) # counted twice each
                    add_top3(s)

        return sorted(res, reverse=True)