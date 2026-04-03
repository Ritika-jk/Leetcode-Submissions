import bisect

class Solution(object):
    def maxWalls(self, robots, distance, walls):
        """
        :type robots: List[int]
        :type distance: List[int]
        :type walls: List[int]
        :rtype: int
        """
        n = len(robots)
        if n == 0:
            return 0

        walls.sort()

        # Pair robots with distances and sort by robot position
        vp = sorted(zip(robots, distance))

        intervals = [[0] * 4 for _ in range(n)]

        for i in range(n):
            pos, d = vp[i]

            left_block = vp[i-1][0] if i > 0 else float('-inf')
            right_block = vp[i+1][0] if i < n - 1 else float('inf')

            intervals[i][0] = max(pos - d, left_block)
            intervals[i][1] = pos
            intervals[i][2] = pos
            intervals[i][3] = min(pos + d, right_block)

        def getCount(l, r):
            # Prevent negative returns when lower bound > upper bound
            if l > r:
                return 0
            
            # bisect_left gives lower_bound, bisect_right gives upper_bound
            it1 = bisect.bisect_left(walls, l)
            it2 = bisect.bisect_right(walls, r)
            return it2 - it1

        dp = [[0] * 2 for _ in range(n)]

        dp[0][0] = getCount(intervals[0][0], intervals[0][1])
        dp[0][1] = getCount(intervals[0][2], intervals[0][3])

        for i in range(1, n):
            l1, r1 = intervals[i][0], intervals[i][1]
            l2, r2 = intervals[i][2], intervals[i][3]

            prev_r_left = intervals[i-1][1]
            prev_r_right = intervals[i-1][3]

            # LEFT
            # Added + 1 to prev_r to avoid double-counting walls on the exact boundary
            addL_from_left = getCount(max(l1, prev_r_left + 1), r1)
            addL_from_right = getCount(max(l1, prev_r_right + 1), r1)

            dp[i][0] = max(
                dp[i-1][0] + addL_from_left,
                dp[i-1][1] + addL_from_right
            )

            # RIGHT
            # Added + 1 to prev_r to avoid double-counting walls on the exact boundary
            addR_from_left = getCount(max(l2, prev_r_left + 1), r2)
            addR_from_right = getCount(max(l2, prev_r_right + 1), r2)

            dp[i][1] = max(
                dp[i-1][0] + addR_from_left,
                dp[i-1][1] + addR_from_right
            )

        return max(dp[n-1][0], dp[n-1][1])