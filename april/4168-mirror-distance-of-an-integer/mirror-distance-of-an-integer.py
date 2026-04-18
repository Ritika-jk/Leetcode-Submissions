class Solution(object):
    def mirrorDistance(self, n):
        revn=str(n)[::-1]
        return abs(n-int(revn))
        """
        :type n: int
        :rtype: int
        """
        