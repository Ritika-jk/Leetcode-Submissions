class Solution(object):
    def resultArray(self, A, k):
        res = freq = [0] * k

        for n in A:
            n %= k
            cur = [0] * k
            cur[n] = 1

            for x, y in enumerate(freq):
                cur[x * n % k] += y

            freq = cur
            for x, y in enumerate(freq):
                res[x] += y

        return res
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        