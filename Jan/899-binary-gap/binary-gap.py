class Solution(object):
    def binaryGap(self, n):
        maxgap =0
        bitpos=0
        lastsetbit=-1
        while bitpos < 31:
            if (n>> bitpos)& 1:
                if(lastsetbit != -1):

                    maxgap =max(maxgap, bitpos -lastsetbit)
                lastsetbit = bitpos
            bitpos +=1
        return maxgap
        """
        :type n: int
        :rtype: int
        """
        