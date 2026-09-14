class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        if rec2[0] >= rec1[2]:
            return False

        if rec2[1] >= rec1[3]:
            return False

        if rec2[2] <= rec1[0]:
            return False

        if rec2[3] <= rec1[1]:
            return False

        return True
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        