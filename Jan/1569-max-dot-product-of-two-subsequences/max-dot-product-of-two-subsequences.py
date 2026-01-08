class Solution:
    def maxDotProduct(self, a, b):
        n, m = len(a), len(b)
        NEG = -10**9
        dp = [[NEG]*(m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                take = a[i-1]*b[j-1] + max(0, dp[i-1][j-1])
                dp[i][j] = max(take, dp[i-1][j], dp[i][j-1])

        return dp[n][m]

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        