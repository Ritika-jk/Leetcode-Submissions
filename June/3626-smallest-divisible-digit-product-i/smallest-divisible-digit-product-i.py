class Solution(object):
    
    def smallestNumber(self, n, t):
        while True:
            ori, mul = n, 1
            while mul != 0 and ori > 0:
                mul *= ori % 10;
                ori //= 10
            if mul % t == 0:
                return n
            n += 1
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        