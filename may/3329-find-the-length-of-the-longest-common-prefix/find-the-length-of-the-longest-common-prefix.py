class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        length = 0
        longest = float('-inf')
        prefix = set()
        
        # Step 1: Store all possible prefixes from arr1 into a set
        for val in arr1:
            if val not in prefix:
                while val > 0:
                    prefix.add(val)
                    val = val // 10
        
        # Step 2: Check each number in arr2 for matching prefixes
        for val in arr2:
            while val > 0:
                # If a prefix from arr2 exists in the prefix set, it's a match
                if val in prefix:
                    if val > longest:
                        longest = val
                    # Found the longest prefix for this number, move to next
                    break
                val //= 10
        
        # Step 3: Count the number of digits in the longest prefix found
        while longest > 0:
            length += 1
            longest //= 10
            
        return length
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        