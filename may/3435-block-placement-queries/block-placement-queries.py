from bisect import bisect_left, bisect_right
from sortedcontainers import SortedList

class FenwickMax:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, idx, val):
        idx += 1
        while idx <= self.n:
            self.bit[idx] = max(self.bit[idx], val)
            idx += idx & -idx

    def query(self, idx):
        idx += 1
        res = 0
        while idx > 0:
            res = max(res, self.bit[idx])
            idx -= idx & -idx
        return res


class Solution:
    def getResults(self, queries):
        MX = 50000

        obstacles = SortedList([0, MX])

        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])

        bit = FenwickMax(MX + 1)

        obs = list(obstacles)
        for i in range(1, len(obs)):
            bit.update(obs[i], obs[i] - obs[i - 1])

        ans = []

        for q in reversed(queries):
            if q[0] == 2:
                _, x, sz = q

                idx = obstacles.bisect_right(x) - 1
                pre = obstacles[idx]

                best = max(bit.query(pre), x - pre)
                ans.append(best >= sz)

            else:
                x = q[1]

                idx = obstacles.bisect_left(x)
                left = obstacles[idx - 1]
                right = obstacles[idx + 1]

                obstacles.remove(x)
                bit.update(right, right - left)

        return ans[::-1]