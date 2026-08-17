class Solution(object):
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        prefix = [0] * (n + 1)
        for i, value in enumerate(stoneValue):
            prefix[i + 1] = prefix[i] + value

        def range_sum(left, right):
            return prefix[right + 1] - prefix[left]

        dp = [[0] * n for _ in range(n)]
        max_left = [[0] * n for _ in range(n)]
        max_right = [[0] * n for _ in range(n)]

        for i in range(n):
            max_left[i][i] = stoneValue[i]
            max_right[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                # Find the largest split where left sum <= right sum.
                low, high = left, right - 1
                split = left - 1

                while low <= high:
                    mid = (low + high) // 2

                    left_sum = range_sum(left, mid)
                    right_sum = range_sum(mid + 1, right)

                    if left_sum <= right_sum:
                        split = mid
                        low = mid + 1
                    else:
                        high = mid - 1

                best = 0

                if split >= left:
                    best = max(best, max_left[left][split])

                    if range_sum(left, split) == range_sum(split + 1, right):
                        best = max(best, max_right[split + 1][right])
                    elif split + 2 <= right:
                        best = max(best, max_right[split + 2][right])
                else:
                    best = max(best, max_right[left + 1][right])

                dp[left][right] = best

                total = range_sum(left, right)

                max_left[left][right] = max(
                    max_left[left][right - 1],
                    dp[left][right] + total
                )

                max_right[left][right] = max(
                    max_right[left + 1][right],
                    dp[left][right] + total
                )

        return dp[0][n - 1]
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        