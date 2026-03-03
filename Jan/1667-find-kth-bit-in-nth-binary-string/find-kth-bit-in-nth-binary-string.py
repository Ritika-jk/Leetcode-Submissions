class Solution(object):
    def findKthBit(self, n, k):

        def binaryStringBuilder(n):
            if n == 1:
                return "0"
            
            prev = binaryStringBuilder(n - 1)
            # Invert: swap 0s and 1s
            inverted = ''.join('1' if c == '0' else '0' for c in prev)
            # Reverse
            reversed_inv = inverted[::-1]
            
            return prev + "1" + reversed_inv
        
        binStr = binaryStringBuilder(n)
        return binStr[k - 1]
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        