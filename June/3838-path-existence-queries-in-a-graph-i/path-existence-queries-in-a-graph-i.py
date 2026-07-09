class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]

    def unite(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        dsu = DSU(n)
        
        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                dsu.unite(i, i - 1)
                
        ans = []
        for u, v in queries:
            ans.append(dsu.find(u) == dsu.find(v))
            
        return ans