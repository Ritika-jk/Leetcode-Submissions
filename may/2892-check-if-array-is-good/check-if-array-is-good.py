class Solution(object):
    def isGood(self, nums):
        n = len(nums) - 1
        seen = set()
        dup = False

        for num in nums:
            if num > n: return False

            if num in seen:
                if num < n or dup: return False
                dup = True
                continue

            seen.add(num)

        return True
        """
        :type nums: List[int]
        :rtype: bool
        """
        