class Solution(object):
    def minElement(self, a):
        return min(sum(map(int,str(v))) for v in a)
        """
        :type nums: List[int]
        :rtype: int
        """
        