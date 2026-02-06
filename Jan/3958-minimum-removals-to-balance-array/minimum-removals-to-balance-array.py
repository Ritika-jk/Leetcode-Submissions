class Solution(object):
    def minRemoval(self, nums, k):
        nums.sort()
        i = 0
        ans = 0
        n = len(nums)

        for j in range(n):
            while nums[i] * k < nums[j]:
                i += 1
            ans = max(ans, j - i + 1)

        return n - ans
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        