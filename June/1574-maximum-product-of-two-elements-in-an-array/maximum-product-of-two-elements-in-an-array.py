class Solution:
    def maxProduct(self, nums):

        max1 = float('-inf')
        max2 = float('-inf')

        min1 = float('inf')
        min2 = float('inf')

        for num in nums:

            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num

            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        p1 = (max1 - 1) * (max2 - 1)
        p2 = (min1 - 1) * (min2 - 1)

        return max(p1, p2)