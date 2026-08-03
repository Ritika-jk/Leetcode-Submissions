class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        sorted_pairs = sorted(zip(nums, range(n)))
        sorted_vals = [p[0] for p in sorted_pairs]
        pos_of = [0] * n
        for pos, (_, orig_idx) in enumerate(sorted_pairs):
            pos_of[orig_idx] = pos
        
        comp = [0] * n
        c = 0
        prev = sorted_vals[0]
        for i in range(1, n):
            cur = sorted_vals[i]
            if cur - prev > maxDiff:
                c += 1
            comp[i] = c
            prev = cur
        
        next_reach = [0] * n
        right = 0
        for i in range(n):
            if right < i:
                right = i
            while right + 1 < n and sorted_vals[right+1] - sorted_vals[i] <= maxDiff:
                right += 1
            next_reach[i] = right
        
        LOG = max(1, (n).bit_length())
        jump = [next_reach]
        for k in range(1, LOG):
            prev_level = jump[-1]
            jump.append([prev_level[prev_level[i]] for i in range(n)])
        
        def min_jumps(i, j):
            if i == j:
                return 0
            if i > j:
                i, j = j, i
            if comp[i] != comp[j]:
                return -1
            steps = 0
            cur = i
            for k in range(LOG-1, -1, -1):
                nxt = jump[k][cur]
                if nxt < j:
                    cur = nxt
                    steps += (1 << k)
            return steps + 1
        
        answer = []
        for u, v in queries:
            pu, pv = pos_of[u], pos_of[v]
            answer.append(min_jumps(pu, pv))
        
        return answer