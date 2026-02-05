class Solution(object):
    def constructTransformedArray(self, nums):
        result = [0] * len(nums)
        n = len(nums)

        for i in range(len(nums)):
            temp = (i + nums[i]) % n
            result[i] = nums[temp]

        return result
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        