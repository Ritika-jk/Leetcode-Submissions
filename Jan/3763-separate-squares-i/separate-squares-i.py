class Solution:
    def getAreaBelow(self, squares, y):
        area = 0.0
        for s in squares:
            yi = s[1]
            length = s[2]

            if y <= yi:
                continue
            elif y >= yi + length:
                area += length * length
            else:
                area += length * (y - yi)

        return area

    def separateSquares(self, squares):
        total_area = 0.0
        min_y = float('inf')
        max_y = 0.0

        for s in squares:
            length = s[2]
            total_area += length * length
            min_y = min(min_y, s[1])
            max_y = max(max_y, s[1] + length)

        low, high = min_y, max_y

        # Binary search for precise y
        for _ in range(100):
            mid = (low + high) / 2.0
            if self.getAreaBelow(squares, mid) < total_area / 2.0:
                low = mid
            else:
                high = mid

        return low
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        