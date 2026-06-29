class Solution(object):
    def numOfStrings(self,a,s):
        return sum(t in s for t in a)
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        