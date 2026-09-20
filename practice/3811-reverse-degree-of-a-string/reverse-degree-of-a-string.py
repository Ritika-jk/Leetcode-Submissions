class Solution(object):
    def reverseDegree(self, s):
        total = 0
        for i, c in enumerate(s):
            reverse_value = 26 - (ord(c) - ord('a'))
            position = i + 1

            total += reverse_value * position
        return total
        """
        :type s: str
        :rtype: int
        """
        