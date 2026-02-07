class Solution(object):
    def minimumDeletions(self, s):
        n = len(s)
        prefix = [0] * n
        suffix = [0] * n

        # 1. Fill prefix array: count 'b's to the left of i
        for i in range(1, n):
            prefix[i] = prefix[i-1] + (1 if s[i-1] == 'b' else 0)

        # 2. Fill suffix array: count 'a's to the right of i
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i+1] + (1 if s[i+1] == 'a' else 0)

        # 3. Calculate minimum deletions
        ans = float('inf')
        for i in range(n):
            ans = min(ans, prefix[i] + suffix[i])
            
        return ans
        """
        :type s: str
        :rtype: int
        """
        