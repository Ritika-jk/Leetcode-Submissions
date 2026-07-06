class Solution(object):
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key=lambda x: (x[0], -x[1]))

        ans = 0
        maxEnd = -1

        for start, end in intervals:
            if end > maxEnd:
                ans += 1
                maxEnd = end

        return ans

#        """
#        :type intervals: List[List[int]]
#        :rtype: int
#        """
#        
