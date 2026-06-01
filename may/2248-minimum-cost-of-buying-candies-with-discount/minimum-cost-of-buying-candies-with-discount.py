class Solution(object):
    def minimumCost(self, cst):
        cst.sort(reverse=True)

        ans = 0

        for i, val in enumerate(cst):
            if i % 3 != 2:
                ans += val

        return ans
        """
        :type cost: List[int]
        :rtype: int
        """
        