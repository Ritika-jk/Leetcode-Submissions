from collections import deque

class Solution:
    MOD = 10**9 + 7

    def func(self, pos, curr_sum_is_odd, depth, dp):
        if pos == depth:
            dp[pos][curr_sum_is_odd] = 1 - curr_sum_is_odd
            return dp[pos][curr_sum_is_odd]

        if dp[pos][curr_sum_is_odd] != -1:
            return dp[pos][curr_sum_is_odd] % self.MOD

        cur_ways = self.func(
            pos + 1,
            1 - curr_sum_is_odd,
            depth,
            dp
        ) % self.MOD

        cur_ways += self.func(
            pos + 1,
            curr_sum_is_odd,
            depth,
            dp
        ) % self.MOD

        dp[pos][curr_sum_is_odd] = cur_ways % self.MOD
        return dp[pos][curr_sum_is_odd]

    def assignEdgeWeights(self, edges):
        n = len(edges) + 1

        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis = [False] * (n + 1)

        depth = 0
        q = deque([1])
        vis[1] = True

        while q:
            sz = len(q)

            for _ in range(sz):
                u = q.popleft()

                for v in adj[u]:
                    if not vis[v]:
                        vis[v] = True
                        q.append(v)

            depth += 1

        depth -= 1

        dp = [[-1] * 2 for _ in range(depth + 1)]

        ans = 0
        ans += self.func(0, 0, depth - 1, dp) % self.MOD
        ans += self.func(0, 1, depth - 1, dp) % self.MOD

        return ans % self.MOD