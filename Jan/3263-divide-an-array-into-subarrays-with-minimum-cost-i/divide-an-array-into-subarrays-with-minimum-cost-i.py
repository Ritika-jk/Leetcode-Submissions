class Solution(object):
    def minimumCost(self, nums):
        ans = nums[0]
        nums[1:] = sorted(nums[1:])
        ans += nums[1]
        ans += nums[2]
        return ans
        """
        :type nums: List[int]
        :rtype: int
        """
        