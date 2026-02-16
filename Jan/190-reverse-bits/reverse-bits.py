class Solution(object):
    def reverseBits(self, n):
        bits=bin(n)[2:]
        bits="0"*(32-len(bits))+bits;
        return int(bits[::-1],2)
        """
        :type n: int
        :rtype: int
        """
        