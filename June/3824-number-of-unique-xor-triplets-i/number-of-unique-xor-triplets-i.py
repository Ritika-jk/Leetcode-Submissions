class Solution(object):
    def uniqueXorTriplets(self, nums):
        n = len(nums)

        if n <= 2:
            return n

        mask = 0
        for num in nums:
            mask |= num

        return mask + 1
        """
        :type nums: List[int]
        :rtype: int
        """
        