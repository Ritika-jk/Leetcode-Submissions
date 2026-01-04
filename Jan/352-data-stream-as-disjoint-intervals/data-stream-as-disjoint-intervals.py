from bisect import bisect_right

class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value) :
        # Optimization: Search for [value + 1]
        # This guarantees we find the position AFTER any interval that starts <= value.
        # Logic: 
        #   If interval starts at 'value', [value, end] < [value + 1] is True.
        #   If interval starts at 'value + 1', [value + 1, end] > [value + 1] is True.
        #   Thus, idx will land exactly between them.
        idx = bisect_right(self.intervals, [value + 1])
        
        # 1. Check overlap with the previous interval (left side)
        merge_left = False
        if idx > 0:
            prev_interval = self.intervals[idx - 1]
            # If value is already covered by the previous interval, do nothing
            if prev_interval[1] >= value:
                return
            # If value is exactly 1 greater than previous end, we can merge
            if prev_interval[1] == value - 1:
                merge_left = True
        
        # 2. Check overlap with the next interval (right side)
        merge_right = False
        if idx < len(self.intervals):
            next_interval = self.intervals[idx]
            # If value is exactly 1 less than next start, we can merge
            if next_interval[0] == value + 1:
                merge_right = True
        
        # 3. Perform Merges
        if merge_left and merge_right:
            # Bridge two intervals: [1, 2] + 3 + [4, 5] -> [1, 5]
            self.intervals[idx - 1][1] = self.intervals[idx][1]
            self.intervals.pop(idx)
        elif merge_left:
            # Extend left: [1, 2] + 3 -> [1, 3]
            self.intervals[idx - 1][1] = value
        elif merge_right:
            # Extend right: 3 + [4, 5] -> [3, 5]
            self.intervals[idx][0] = value
        else:
            # No merge, insert new interval: [1, 1], 3 -> [1, 1], [3, 3]
            self.intervals.insert(idx, [value, value])

    def getIntervals(self): 
        return self.intervals