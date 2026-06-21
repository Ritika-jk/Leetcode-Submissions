class Solution(object):
    def maxIceCream(self, costs, coins):
        costs.sort()

        count = 0

        for cost in costs:
            if cost > coins:
                break

            count += 1
            coins -= cost

        return count
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        