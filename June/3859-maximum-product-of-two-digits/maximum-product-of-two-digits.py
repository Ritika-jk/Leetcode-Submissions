class Solution(object):
    def maxProduct(self, n):
        f = s = 0

        while n:
            d = n % 10

            if d >= f:
                s = f
                f = d
            elif d > s:
                s = d

            n //= 10

        return f * s
        """
        :type n: int
        :rtype: int
        """
        