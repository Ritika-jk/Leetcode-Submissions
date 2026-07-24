class Solution(object):
    def uniqueXorTriplets(self, nums):
        n = len(nums)

        if n < 3:
            return len(set(nums))

        MAXX = 2048

        values = list(set(nums))

        pair_xor = set()

        for a in values:
            for b in values:
                pair_xor.add(a ^ b)

        triplet_xor = set()

        for x in pair_xor:
            for v in values:
                triplet_xor.add(x ^ v)

        return len(triplet_xor)
        """
        :type nums: List[int]
        :rtype: int
        """
        