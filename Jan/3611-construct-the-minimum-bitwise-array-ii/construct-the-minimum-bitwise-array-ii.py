class Solution(object):
    def minBitwiseArray(self, values):

        res = []

        for cur in values:
            if cur == 2:
                res.append(-1)
                continue

            temp = cur
            cnt = 0

            while temp & 1:
                cnt += 1
                temp >>= 1

            res.append(cur - (1 << (cnt - 1)))

        return res
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        