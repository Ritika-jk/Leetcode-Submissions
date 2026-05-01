class Solution(object):
    def maxRotateFunction(self, nums):
        def F(arr) :
            f = 0
            for i in range(len(arr)):
                f += (i * arr[i])
            return f
        
        n = len(nums)
        total_sum = sum(nums)

        dp = [F(nums)]
        
        for i in range(1, n):
            curr = dp[i - 1] + total_sum - n * nums[n - i]
            dp.append(curr)

        return max(dp)
        """
        :type nums: List[int]
        :rtype: int
        """
        