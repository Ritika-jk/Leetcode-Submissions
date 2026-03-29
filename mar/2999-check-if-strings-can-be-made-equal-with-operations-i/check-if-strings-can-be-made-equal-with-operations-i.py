class Solution(object):
    def canBeEqual(self, s1, s2):
        a = sorted([s1[0], s1[2]])
        b = sorted([s1[1], s1[3]])
        c = sorted([s2[0], s2[2]])
        d = sorted([s2[1], s2[3]])
        return a == c and b == d
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        