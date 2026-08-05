class Solution(object):
    def remainingMethods(self, n, k, invocations):
        g = [[] for _ in range(n)]
        for a, b in invocations:
            g[a].append(b)

        suspicious = [False] * n
        stack = [k]
        suspicious[k] = True

        while stack:
            u = stack.pop()
            for v in g[u]:
                if not suspicious[v]:
                    suspicious[v] = True
                    stack.append(v)

        for a, b in invocations:
            if not suspicious[a] and suspicious[b]:
                return list(range(n))

        return [i for i in range(n) if not suspicious[i]]
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        