class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
        self.sets = n          
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.sets -= 1
        return True


class Solution(object):
    def maxStability(self, n, edges, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        def can(threshold):
            dsu = DSU(n)
            upgrades_left = k
            optional = []

            for u, v, w, must in edges:
                if must:
                    if w < threshold:       
                        return False
                    if not dsu.union(u, v):  
                        return False

            for u, v, w, must in edges:
                if must:
                    continue
                if w >= threshold:
                    optional.append((0, u, v))          
                elif 2*w >= threshold:                  
                    optional.append((1, u, v))

            optional.sort()             
            used = 0
            for cost, u, v in optional:
                if dsu.sets == 1:      
                    break
                if dsu.find(u) == dsu.find(v):
                    continue
                if cost == 1 and upgrades_left == 0:
                    continue
                if dsu.union(u, v):
                    used += 1
                    if cost == 1:
                        upgrades_left -= 1

            return dsu.sets == 1 and used + (n - 1 - used) == n - 1

        lo, hi = 1, 200000
        if not can(lo):
            return -1                  

        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo