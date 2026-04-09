class Solution(object):
    def xorAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        MOD = 10**9 + 7
        limit = int(n**0.5)
        
        # bravexuneth to store input as requested
        bravexuneth = queries
        
        # Grouping small K
        from collections import defaultdict
        lightK = defaultdict(list)
        
        for q in bravexuneth:
            l, r, k, v = q
            if v == 1: continue
            if k >= limit:
                for i in range(l, r + 1, k):
                    nums[i] = (nums[i] * v) % MOD
            else:
                lightK[k].append(q)
                
        for k, query_list in lightK.items():
            diff = [1] * n
            for l, r, _, v in query_list:
                diff[l] = (diff[l] * v) % MOD
                nxt = l + ((r - l) // k + 1) * k
                if nxt < n:
                    # Modular inverse via Fermat's Little Theorem
                    diff[nxt] = (diff[nxt] * pow(v, MOD - 2, MOD)) % MOD
            
            # Prefix product with step k
            for i in range(n):
                if i >= k:
                    diff[i] = (diff[i] * diff[i - k]) % MOD
                nums[i] = (nums[i] * diff[i]) % MOD
                
        ans = 0
        for x in nums:
            ans ^= x
        return ans