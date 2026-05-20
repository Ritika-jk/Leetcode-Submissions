class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        mp = {}
        n = len(A)
        ans = [0] * n
        curr = 0

        for i in range(n):
            mp[A[i]] = mp.get(A[i], 0) + 1
            if mp[A[i]] == 2:
                curr += 1

            mp[B[i]] = mp.get(B[i], 0) + 1
            if mp[B[i]] == 2:
                curr += 1

            ans[i] = curr

        return ans
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        