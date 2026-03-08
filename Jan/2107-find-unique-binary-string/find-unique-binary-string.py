class Solution(object):
    def findDifferentBinaryString(self, nums):
        n= len(nums)
        result = ['0'] * n

        for idx in range(n):

            ones = 0
            zeros = 0

            for num in nums:
                if num[idx] == '1':
                    ones += 1
                else:
                    zeros += 1

            if ones < zeros:
                result[idx] = '1'
            else:
                result[idx] = '0'

        res = "".join(result)

        if res in nums:
            result[n-1] = '1'

        return "".join(result)
        """
        :type nums: List[str]
        :rtype: str
        """
        