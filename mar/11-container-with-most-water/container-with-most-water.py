class Solution(object):
    def maxArea(self, height):
        n = len(height)
        
        i=0 
        j=n-1
        res = 0
        while i<j:

            res = max(res, (j-i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i+=1
            else :
                j-=1
        return res

        
        
        
        """
        :type height: List[int]
        :rtype: int
        """
        