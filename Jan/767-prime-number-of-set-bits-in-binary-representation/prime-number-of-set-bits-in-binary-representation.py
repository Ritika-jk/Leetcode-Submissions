class Solution(object):
    def countSetBits(self,n):
        count = 0
        while n > 0:
            n &= (n - 1)  # clears the rightmost set bit
            count += 1    # increment for each bit cleared
        return count

    def countPrimeSetBits(self, left, right) :
        cntPrimeSetBits = 0
        # The mask represents primes: 2, 3, 5, 7, 11, 13, 17, 19
        magicMask = 665772

        for num in range(left, right + 1):
            if (magicMask >> self.countSetBits(num)) & 1:
                cntPrimeSetBits += 1

        return cntPrimeSetBits
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        