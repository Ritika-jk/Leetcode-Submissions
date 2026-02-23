class Solution(object):
    def hasAllCodes(self, s, k):
        actual = 1 << k

        if len(s) - k + 1 < actual:
            return False

        seen = set()

        for i in range(len(s) - k + 1):
            seen.add(s[i:i+k])

        return len(seen) == actual
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        