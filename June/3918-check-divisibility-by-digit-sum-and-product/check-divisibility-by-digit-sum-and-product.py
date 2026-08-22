class Solution(object):
    def checkDivisibility(self, n):
        a = n
        d_sum = 0
        d_prod = 1

        while a != 0:
            dig = a % 10
            d_sum += dig
            d_prod *= dig
            a //= 10

        return n % (d_sum + d_prod) == 0
        """
        :type n: int
        :rtype: bool
        """
        