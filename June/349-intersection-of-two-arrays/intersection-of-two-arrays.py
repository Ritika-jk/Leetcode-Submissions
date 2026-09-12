class Solution(object):
    def intersection(self, nums1, nums2):
        a = set(nums1)
        b = set(nums2)
        return list(set(a & b))
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        