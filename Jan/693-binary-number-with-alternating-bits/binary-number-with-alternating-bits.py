class Solution(object):
    def hasAlternatingBits(self, n):
        number =n^ (n>>1)
        return (number& (number +1))==0
        n=6
        print(hasAlternateingBits(n))
        """
        :type n: int
        :rtype: bool
        """
        