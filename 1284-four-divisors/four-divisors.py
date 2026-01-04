class Solution(object):
    def sumFourDivisors(self, nums):
        total_sum = 0
        
        for num in nums:
            found_divisor = 0
            divisor = 2
            
            while divisor * divisor <= num:
                if num % divisor == 0:
                    if found_divisor == 0:
                        found_divisor = divisor
                    else:
                        found_divisor = 0
                        break
                divisor += 1
            
            if found_divisor > 0 and found_divisor != num // found_divisor:
                total_sum += 1 + num + found_divisor + num // found_divisor
        
        return total_sum
        """
        :type nums: List[int]
        :rtype: int
        """
        