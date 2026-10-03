class Solution(object):
    def largestRectangleArea(self, heights):
        res = 0
        st =[]
        n= len(heights)
        i=0

        while i<n:
            start = i
            while st and st[-1][0] >= heights[i]:
                v, j = st.pop()
                res = max( res , v*(i-j))
                start = j
            st.append([heights[i], start])
            i+=1
        while st: 
            v, j = st.pop()
            res = max(res, v *(n - j))  
        return res 
        """
        :type heights: List[int]
        :rtype: int
        """
        